import numpy as np
import sounddevice as sd
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['toolbar'] = 'toolmanager'

# faz a detecçao automatica do dispositivo de entrada
def get_default_input_device():
    try:
        default = sd.default.device[0]

        if default is None or default < 0:
            raise Exception("Nenhum dispositivo padrão")

        info = sd.query_devices(default)

        if info['max_input_channels'] < 1:
            raise Exception("Dispositivo padrão não tem entrada")

        return default, info

    except:
        devices = sd.query_devices()

        for i, dev in enumerate(devices):
            if dev['max_input_channels'] > 0:
                return i, dev

        raise RuntimeError("Nenhum microfone encontrado")

device_id, device_info = get_default_input_device()
fs = int(device_info['default_samplerate'])

block = 4096
bands = 64

audio_buffer = np.zeros(block)
prev_values = np.zeros(bands)
alpha = 0.5

time_ylim = [-1, 1]
spec_ylim = 1.0

zoom_alpha = 0.2
decay = 0.85
MIN_RANGE = 0.007

def freq_to_note(freq):
    if freq <= 0:
        return ""

    A4 = 440
    note_names = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

    n = int(round(12 * np.log2(freq / A4)))
    note_index = (n + 9) % 12
    octave = 4 + (n + 9) // 12

    return f"{note_names[note_index]}{octave}"

def audio_callback(indata, frames, time, status):
    global audio_buffer

    if status:
        print(status)

    if len(indata) >= block:
        audio_buffer = indata[:block, 0].copy()
    else:
        padded = np.zeros(block)
        padded[:len(indata)] = indata[:, 0]
        audio_buffer = padded

stream = sd.InputStream(
    device=device_id,
    channels=1,
    samplerate=fs,
    dtype='float32',
    blocksize=block,
    callback=audio_callback
)

stream.start()

# graficos
plt.style.use("dark_background")

fig, (ax_time, ax_freq) = plt.subplots(2, 1, figsize=(10, 7))

# permite interação só no gráfico de cima, para poder dar zoom e pan para ver mais bonito as ondas no front
ax_time.set_navigate(True)
ax_freq.set_navigate(False)

time_line, = ax_time.plot(np.zeros(block))
ax_time.set_title("Sinal no Tempo")

x = np.arange(bands)
bars = ax_freq.bar(x, np.zeros(bands))

for bar in bars:
    bar.set_alpha(0.8)

ax_freq.set_xlim(0, bands)
peak_marker = ax_freq.axvline(0, color="red", linewidth=2, alpha=0.8)

def update(frame):

    global audio_buffer, prev_values, time_ylim, spec_ylim

    audio = audio_buffer

    if len(audio) == 0:
        return

    time_line.set_ydata(audio)
    #abrir no artigo (remover média para evitar offset)
    audio = audio - np.mean(audio)

    #abrir no artigo aplica janela de Hanning que reduz o efeito de "vazamento espectral" que ocorre porque estamos analisando um sinal finito no tempo
    window = np.hanning(len(audio))
    audio = audio * window

    #abrir no artigo  FFT (Fast Fourier Transform) aqui aplica a Transformada Discreta de Fourier (DFT)
    # abrir no artigo utilizando o algoritmo eficiente FFT (O(N log N)) colocar pra bonito e tals
    # abrir conceitos matematicos e mostrar formulas e tals
    fft = np.fft.rfft(audio)
    #abrir no artigo a fft retorna numero complexos, no caso a amplitude de cada frequencia e a fase, mas a gente só quer a amplitude, por isso o np.abs() que calcula a magnitude do número complexo, que representa a intensidade da frequência correspondente
    magnitude = np.abs(fft)

    #abrir no artigo evita divisão por zero
    if np.max(magnitude) == 0:
        return

    #abrir no artigo escala para ficar entre 0 e 1, o que facilita a visualização e comparação das bandas
    magnitude /= np.max(magnitude)
    #abrir no artigo eixo de frequencias correspondente a cada componente da FFT, calculado com np.fft.rfftfreq() que retorna as freq para a FFT real, considerando a taxa de amostragem fs e o tamanho do audio
    freqs = np.fft.rfftfreq(len(audio), 1/fs)
    #abrir no artigo encontra a frequencia dominante, ou seja
    peak_index = np.argmax(magnitude[1:]) + 1
    #abrir no artigo aqui pega  freq dominante, no caso a nota musical
    peak_freq = freqs[peak_index]
    note = freq_to_note(peak_freq)

    split = np.array_split(magnitude, bands)
    values = np.array([np.mean(b) for b in split])

    values = np.maximum(values, prev_values * decay)
    values = alpha * values + (1 - alpha) * prev_values
    prev_values = values

    for bar, val in zip(bars, values):
        bar.set_height(val)

    # zoom no tempo (com minimo)
    min_val = np.min(audio)
    max_val = np.max(audio)

    range_val = max_val - min_val

    if range_val < MIN_RANGE:
        center = (max_val + min_val) / 2
        min_val = center - MIN_RANGE / 2
        max_val = center + MIN_RANGE / 2
        range_val = MIN_RANGE

    margin = 0.25 * range_val

    target_min = min_val - margin
    target_max = max_val + margin

    time_ylim[0] = (1 - zoom_alpha) * time_ylim[0] + zoom_alpha * target_min
    time_ylim[1] = (1 - zoom_alpha) * time_ylim[1] + zoom_alpha * target_max

    ax_time.set_ylim(time_ylim)

    # zoom na freq
    max_spec = np.max(values)

    if max_spec < MIN_RANGE:
        max_spec = MIN_RANGE

    target_spec = max_spec * 1.33
    spec_ylim = (1 - zoom_alpha) * spec_ylim + zoom_alpha * target_spec

    ax_freq.set_ylim(0, spec_ylim)

    # pico
    peak_band = int((peak_index / len(magnitude)) * bands)
    peak_marker.set_xdata([peak_band])

    peak_marker.set_alpha(0.6 + 0.4 * max_spec)

    ax_freq.set_title(f"{peak_freq:.1f} Hz | Nota: {note}")

ani = FuncAnimation(fig, update, interval=30)

plt.tight_layout()
plt.show()