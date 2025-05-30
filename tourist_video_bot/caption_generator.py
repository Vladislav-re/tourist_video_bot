
import os
import openai

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.base_url = "https://openrouter.ai/api/v1"

def generate_caption(location):
    prompt = f"Придумай увлекательное описание к туристическому видео с локацией '{location}' в стиле тревел-блога."

    response = openai.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
