from PIL import Image, ImageDraw, ImageFont 
import os
input_path = '/data/output/resized.jpg'
output_path='/data/output/watermarked.jpg'
print("Adding watermark...")
image = Image.open(input_path)
draw = ImageDraw.Draw(image)
font =  ImageFont.load_default()
draw.text((50,50),"Sample watermark ",fill=(0,255,128),font=font)
image.save(output_path)
print("Watermarked image saved!")

