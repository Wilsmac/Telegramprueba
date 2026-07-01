from telegram import Update
from telegram.ext import ContextTypes

from database.database import borrar
from memory.memory import cache
from utils.config import cargar_config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "¡Hola! Soy tu asistente con IA."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
"""
Comandos:

/start
/help
/reset
"""
    )

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat=update.effective_chat.id

    borrar(chat)

    cache[chat]=[]

    await update.message.reply_text(
        "Memoria eliminada."
    )
  async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong")
   
 async def config(update, context):

    cfg = cargar_config()

    texto = ""

    for k,v in cfg.items():
        texto += f"{k}: {v}\n"

    await update.message.reply_text(texto)
