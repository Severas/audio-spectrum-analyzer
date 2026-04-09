# 🎧 Audio Spectrum Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/OS-Linux%20%7C%20Windows-green">
  <img src="https://img.shields.io/badge/Status-Ativo-success">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## 📌 Sobre o Projeto

Este projeto realiza a **análise de áudio em tempo real** utilizando a Transformada de Fourier (FFT), exibindo:

- 📈 Sinal no domínio do tempo  
- 📊 Espectro de frequências  
- 🎼 Frequência dominante + nota musical  

---

## 📄 Artigo

O artigo completo deste projeto pode ser acessado aqui:

👉 [📥 Baixar artigo (PDF)](docs/artigo.pdf)

---

## 🚀 Navegação Rápida

- [📂 Estrutura](#-estrutura-do-projeto)
- [⚙️ Instalação (Arch Linux)](#️-arch-linux)
- [🪟 Instalação (Windows)](#-windows)
- [▶️ Execução](#️-execução)
- [🖱️ Como usar](#️-como-usar)
- [🧠 Funcionamento](#-funcionamento)
- [📚 Base Teórica](#-base-teórica)
- [❗ Problemas comuns](#-problemas-comuns)

---

## 📂 Estrutura do Projeto

```
projeto/
│
├── spectrum_analyzer.py
├── requirements.txt
├── README.md
├── LICENSE
└── docs/
    └── artigo.pdf
```

---

## ⚙️ Arch Linux

```bash
sudo pacman -S python python-pip portaudio
```

Opcional:

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

1. Instale Python: https://www.python.org/downloads/  
2. Marque **Add Python to PATH**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Execução

```bash
python spectrum_analyzer.py
```

---

## 🖱️ Como usar

| Ação        | Como fazer |
|------------|-----------|
| 🔍 Zoom     | Botão de lupa + arrastar |
| ✋ Pan      | Arrastar gráfico |
| 🔄 Reset    | Botão Home |

---

## 🧠 Funcionamento

O sistema:

1. Captura áudio do microfone  
2. Aplica Transformada de Fourier (FFT)  
3. Calcula o espectro de frequências  
4. Detecta a frequência dominante  

---

## 📚 Base Teórica

Este projeto foi desenvolvido com base nos conceitos de:

- Transformada de Fourier  
- Processamento Digital de Sinais  
- Análise espectral de áudio  

Os detalhes completos estão descritos no artigo incluído neste repositório.

---

## ❗ Problemas comuns

```bash
sudo pacman -S portaudio
```

---

## 👨‍💻 Autor

David Marcelo Gois  
GitHub: https://github.com/Severas

---

## 📄 Licença

Este projeto está sob a licença MIT.
