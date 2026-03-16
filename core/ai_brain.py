import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

TOKEN = "YOUR_HUGGINGFACE_TOKEN"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def ask_ai(prompt):

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    return response.json()
