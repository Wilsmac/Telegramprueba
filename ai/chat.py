from openai import OpenAI
from config import OPENAI_KEY, MODEL

client = OpenAI(api_key=OPENAI_KEY)

with open("prompts/system.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def preguntar(historial):

    entrada = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    entrada.extend(historial)

    respuesta = client.responses.create(
        model=MODEL,
        input=entrada
    )

    return respuesta.output_text
