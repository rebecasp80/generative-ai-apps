# 🎙️ Generative AI Voice Assistant — Traductor de Voz con Flask + Groq + LangChain

Este proyecto implementa un asistente de voz inteligente capaz de escuchar, transcribir, traducir y hablar en múltiples idiomas utilizando Groq, LangChain 1.x y un servidor Flask.

Incluye una interfaz web moderna estilo Minimal Tech Noir, con diseño elegante, tonos oscuros y acentos cian, ofreciendo una experiencia fluida y profesional para traducción automática.

Forma parte del repositorio Generative AI Apps, donde se desarrollan aplicaciones de IA generativa para portafolios profesionales.

---

## 🚀 Características principales

🎤 Reconocimiento de voz (STT)  

Convierte voz a texto mediante la Web Speech API del navegador.

🔊 Síntesis de voz (TTS)  

El asistente pronuncia la traducción en el idioma destino seleccionado.

🌐 Traducción automática con Groq + LangChain  

Traducción rápida y precisa utilizando:

Groq (modelo llama‑3.1‑8b‑instant)

LangChain 1.x

Arquitectura moderna basada en Runnables

🧠 Detección automática del idioma origen  

El sistema identifica el idioma del texto o voz de entrada y traduce sin necesidad de selección manual.

🌍 Selector de idioma destino  

Traducción disponible a:

Español · Inglés · Francés · Alemán · Italiano · Portugués · Japonés · Chino · Ruso · Árabe

🎨 Interfaz Minimal Tech Noir

Diseño moderno y profesional con:

Fondo oscuro y acentos cian

Contenedores blur con bordes luminosos

Botones minimalistas y animaciones suaves

Chat estilizado con scroll automático

Experiencia visual premium y fluida

⚡ Servidor Flask

Rutas:

/ → interfaz web

/translate → procesamiento de traducción

---

## 📁 Estructura del proyecto

Código

generative-ai-voice-assistant/

│

├── app.py                 # Servidor Flask

├── worker.py              # Traducción con Groq + LangChain

│

├── templates/

│   └── index.html         # Interfaz Minimal Tech Noir

│

├── static/

│   ├── style.css          # Estilos modernos

│   └── script.js          # Lógica del frontend (STT, TTS, fetch)

│

└── .env                   # API Key de Groq

---

## 🔧 Requisitos

Instala las dependencias dentro de tu entorno virtual (venv310):

bash

pip install flask langchain langchain-core langchain-community langchain-groq faiss-cpu sentence-transformers python-dotenv langdetect

---

## 🔑 Configuración de la API de Groq

En tu archivo .env:

bash

GROQ_API_KEY=tu_clave_aquí

Modelo utilizado:

bash

llama-3.1-8b-instant

▶️ Ejecutar el asistente de voz

Desde la carpeta del proyecto:

bash

python app.py

Luego abre en tu navegador:

Código

http://127.0.0.1:5000

---

## 🧠 Rutas del servidor

GET /  

Renderiza la interfaz web.

POST /translate  

Recibe texto, detecta idioma origen, traduce al idioma destino y devuelve la respuesta.

---

## 🎨 Interfaz web (Minimal Tech Noir)

Incluye:

Fondo oscuro con acentos cian

Contenedores blur y bordes luminosos

Botones minimalistas y animaciones suaves

Selector de idiomas

Chat estilizado con scroll automático

Micrófono integrado

TTS automático

Diseñada para transmitir una estética tecnológica, elegante y profesional.

---

## 📌 Objetivo del proyecto

Este módulo forma parte del repositorio Generative AI Apps, demostrando habilidades en:

IA generativa

Traducción automática

Flask

Groq

LangChain 1.x

Diseño web moderno

Integración STT + TTS

Aplicaciones interactivas

---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa.

Repositorio: Generative AI Apps

Tecnologías: Python · Flask · Groq · LangChain · HTML/CSS · JavaScript

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT incluida en el repositorio principal.
