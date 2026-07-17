# 🗣️ Enterprise Meeting Companion — AI Meeting Analyzer (Groq + Whisper + Gradio)

Aplicación de **IA generativa** que analiza reuniones empresariales a partir de archivos de audio.  

Utiliza **Whisper** para transcripción automática y **Groq Llama 3.1** para generar análisis inteligentes con resumen, decisiones y tono general.  

La interfaz está construida con **Gradio**, y el proyecto está preparado para despliegue en entornos cloud.

---

## 🚀 Características principales

- 🎤 **Transcripción automática** con Whisper (faster‑whisper).  

- 🧠 **Análisis inteligente** con Groq Llama 3.1.  

- 📊 **Resumen, decisiones y acciones** generadas por IA.  

- 🖥️ **Interfaz Gradio** intuitiva y lista para producción.  

- 🔐 **Gestión segura de API Key** mediante `.env`.

---

## 📂 Estructura del proyecto

enterprise-meeting-companion/

│

├── speech_analyzer.py

├── simple_llm_groq.py

├── download_audio.py

├── simple_speech2text.py

├── speech2text_app.py

├── requirements.txt

├── .gitignore

└── README.md

---

## 🧠 Modelos utilizados

Groq Llama 3.1‑8B‑Instant → análisis semántico y generación de texto.

Whisper (small) → transcripción de audio rápida y precisa.

---

## 🛠️ Instalación y ejecución local

Desde la carpeta del proyecto:

cd enterprise-meeting-companion

python -m venv venv310

venv310\Scripts\activate      # En Windows

pip install -r requirements.txt

python speech_analyzer.py

La interfaz estará disponible en:

👉 http://127.0.0.1:7860


---

## 🐳 Ejecución con Docker (opcional)

docker build -t meeting-analyzer-app .

docker run -p 7860:7860 meeting-analyzer-app

---

## 🧩 Variables de entorno

Crea un archivo .env con tu clave de Groq:

GROQ_API_KEY=gsk_tu_api_key_aqui

---

## 🪄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.
