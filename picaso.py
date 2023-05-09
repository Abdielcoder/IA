import openai
import requests
from requests.structures import CaseInsensitiveDict

openai.api_key = "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"

def generate_image(prompt):
    url = "https://api.openai.com/v1/images/generations"

    model = "image-alpha-001"
    data = {
        "model": model,
        "prompt": prompt,
        "num_images": 1,
        "size": "256x256",
        "response_format": "url"
    }

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {openai.api_key}"

    resp = requests.post(url, json=data, headers=headers)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_data = resp.json()["data"][0]
    return response_data["url"]

image_url = generate_image("Dame una imagen de una persona preocupada por que choco")
print(image_url)
