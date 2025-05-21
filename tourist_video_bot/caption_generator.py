import os
import openai

def generate_caption(location: str) -> str:
    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    prompt = f"Придумай дерзкое, ироничное, но короткое описание туристического видео из {location}. Без эмодзи, без лишних слов."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
