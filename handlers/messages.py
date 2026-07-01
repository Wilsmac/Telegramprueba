from telegram import Update
from telegram.ext import ContextTypes

from ai.chat import preguntar
from memory.memory import obtener
from database.database import guardar

async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat=update.effective_chat.id

    historial=obtener(chat)

    texto=update.message.text

    historial.append({
        "role":"user",
        "content":texto
    })

    guardar(chat,"user",texto)

    respuesta=preguntar(historial)

    historial.append({
        "role":"assistant",
        "content":respuesta
    })

    guardar(chat,"assistant",respuesta)

    await update.message.reply_text(respuesta)
