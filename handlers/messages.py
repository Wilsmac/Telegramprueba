from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import logger

from ai.chat import preguntar
from memory.memory import obtener
from database.database import guardar

async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    if not update.message or not update.message.text:
    return
    
    chat=update.effective_chat.id

    historial=obtener(chat)

    texto=update.message.text

    historial.append({
        "role":"user",
        "content":texto
    })

    guardar(chat,"user",texto)

    try:
    respuesta = preguntar(historial)

except Exception as e:
    logger.exception(e)

    await update.message.reply_text(
        "❌ Ocurrió un error interno."
    )

    return

    historial.append({
        "role":"assistant",
        "content":respuesta
    })

    guardar(chat,"assistant",respuesta)

    await update.message.reply_text(respuesta)
