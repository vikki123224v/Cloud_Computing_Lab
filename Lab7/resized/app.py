from PIL import Image
import os
input_path = '/data/input/image.jpg'
output_path = '/data/output/resized.jpg'
print("Resizing image...")
image = Image.open(input_path)
image = image.resize((300,300))
image.save(output_path)
print("Image resized and saved!")

