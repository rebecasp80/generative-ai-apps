FROM python:3.10-slim

# Evitar errores de certificados
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

# Copiar archivos
COPY requirements.txt .
COPY image_captioning_app.py .
COPY images ./images

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto de Gradio
EXPOSE 7860

# Ejecutar la app
CMD ["python", "image_captioning_app.py"]
