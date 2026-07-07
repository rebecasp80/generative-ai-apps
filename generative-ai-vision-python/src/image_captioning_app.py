# Image Captioning App con Gradio y BLIP
# Autor: Selene

import gradio as gr
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# 1️⃣ Cargar modelo y procesador
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 2️⃣ Función para generar subtítulo
def caption_image(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# 3️⃣ Crear interfaz Gradio
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="pil", label="Sube una imagen"),
    outputs=gr.Textbox(label="Descripción generada"),
    title="Generador de subtítulos con BLIP",
    description="Sube una imagen y obtén una descripción automática generada por IA."
)

# 4️⃣ Ejecutar aplicación
iface.launch(server_name="0.0.0.0", server_port=7860)

