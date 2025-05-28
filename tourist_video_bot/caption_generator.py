
import openai
import os

def generate_caption(location):
    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    prompt = f"Придумай интересное описание туристического видео о {location}."
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()
