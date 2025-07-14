import requests
import vision_config
import io
from PIL import Image, ImageDraw

def analyze_image(image_path):
    analyze_url = vision_config.AZURE_ENDPOINT + "vision/v3.2/analyze"
    headers = {
        'Ocp-Apim-Subscription-Key': vision_config.AZURE_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params = {'visualFeatures': 'Tags,Objects'}
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    return response.json()

def draw_boxes(image_path, analysis):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    for obj in analysis.get("objects", []):
        rect = obj['rectangle']
        left, top, width, height = rect['x'], rect['y'], rect['w'], rect['h']
        draw.rectangle([left, top, left + width, top + height], outline="red", width=3)
        draw.text((left, top - 10), obj['object'], fill="red")
    return image
