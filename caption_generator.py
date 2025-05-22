
import os
import openai

def generate_caption(title):
    key = os.getenv("OPENROUTER_API_KEY")
    openai.api_key = key
    openai.api_base = "https://openrouter.ai/api/v1"

    prompt = f"Напиши шуточное, но информативное описание туристического видео под названием: '{title}' с указанием интересной локации."

    response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
