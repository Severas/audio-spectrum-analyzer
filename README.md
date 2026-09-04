# 🎧 Audio Spectrum Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/OS-Linux%20%7C%20Windows-green">
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## 📌 About the Project

This project performs **real-time audio analysis** using the Fourier Transform (FFT), displaying:

- 📈 Time-domain signal
- 📊 Frequency spectrum
- 🎼 Dominant frequency + musical note

---

## 🚀 Quick Navigation

- [📂 Structure](#-project-structure)
- [⚙️ Installation (Arch Linux)](#️-arch-linux)
- [🪟 Installation (Windows)](#-windows)
- [▶️ Running](#️-running)
- [🖱️ How to Use](#️-how-to-use)
- [🧠 How It Works](#-how-it-works)
- [📚 Theoretical Background](#-theoretical-background)
- [❗ Common Issues](#-common-issues)

---

## 📂 Project Structure

```
project/
│
├── spectrum_analyzer.py
├── requirements.txt
├── README.md
├── LICENSE
```

---

## ⚙️ Arch Linux

```bash
sudo pacman -S python python-pip portaudio
```

Optional:

```bash
sudo pacman -S python-pyqt6
```

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🪟 Windows

1. Install Python: https://www.python.org/downloads/
2. Check **Add Python to PATH**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Running

```bash
python spectrum_analyzer.py
```

---

## 🖱️ How to Use

| Action      | How to do it |
|------------|-----------|
| 🔍 Zoom     | Magnifying glass button + drag |
| ✋ Pan      | Drag the graph |
| 🔄 Reset    | Home button |

---

## 🧠 How It Works

The system:

1. Captures audio from the microphone
2. Applies the Fourier Transform (FFT)
3. Calculates the frequency spectrum
4. Detects the dominant frequency

---

## 📚 Theoretical Background

This project was developed based on the concepts of:

- Fourier Transform
- Digital Signal Processing
- Audio spectral analysis

Full details are described in the paper included in this repository.

---

## ❗ Common Issues

```bash
sudo pacman -S portaudio
```

---

## 👨‍💻 Author

David Marcelo Gois
GitHub: https://github.com/Severas

---

## 📄 License

This project is licensed under the MIT License.
