# BLIP Image Captioning - Proyecto Generative AI Vision Python
# Autor: Selene
# Descripción: Genera subtítulos automáticos para imágenes usando el modelo BLIP de Hugging Face.

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("🔄 Cargando modelo BLIP...")

# 1️⃣ Cargar el modelo y el procesador
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

print("✅ Modelo cargado correctamente.")
print("🔍 Cargando imagen...")

# 2️⃣ Cargar una imagen local (guárdala en la carpeta 'images')
image_path = "images/ejemplo.jpg"  # Cambia el nombre si tu imagen es distinta
image = Image.open(image_path)

print("✅ Imagen cargada correctamente.")
print("🧠 Generando descripción...")

# 3️⃣ Generar subtítulo automático
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

# 4️⃣ Mostrar resultado
print("🖼️ Imagen:", image_path)
print("💬 Descripción generada:", caption)
