
import os
import openai

def generate_caption(location):
    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    prompt = f"Напиши короткий, дерзкий или ироничный комментарий к туристическому видео, снятому в месте: {location}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()
