from openai import OpenAI
from config import OPENAI_KEY, MODEL

client = OpenAI(api_key=OPENAI_KEY)

def preguntar(historial):

    respuesta = client.responses.create(
        model=MODEL,
        input=historial
    )

    return respuesta.output_text
