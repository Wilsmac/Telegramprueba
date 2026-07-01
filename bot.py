from telegram.ext import (
Application,
MessageHandler,
filters
)

from handlers.messages import mensaje
from config import TOKEN

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        mensaje
    )
)

print("Bot iniciado...")

app.run_polling()
