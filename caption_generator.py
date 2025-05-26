
import os
from openai import OpenAI

def generate_caption(location):
    client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"))
    prompt = f"Придумай короткий ироничный комментарий к туристическому видео, снятому в {location}. Без подписей, без имён, от лица обычного туриста."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Failed to generate caption: {e}")
        return "Турист попал в приключение. Смотрите сами!"
