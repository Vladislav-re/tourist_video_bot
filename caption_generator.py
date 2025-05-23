
import openai
import os

def generate_caption(location):
    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    prompt = f"Придумай короткий, ироничный текст к туристическому видео. Локация: {location}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100,
    )
    return response.choices[0].message["content"]
