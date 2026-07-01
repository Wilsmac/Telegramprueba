from telegram import Update
from telegram.ext import ContextTypes

from ai.chat import preguntar
from memory.memory import obtener

async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat = update.effective_chat.id

    historial = obtener(chat)

    historial.append({
        "role":"user",
        "content":update.message.text
    })

    respuesta = preguntar(historial)

    historial.append({
        "role":"assistant",
        "content":respuesta
    })

    await update.message.reply_text(respuesta)
