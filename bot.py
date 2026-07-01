from telegram.ext import (
Application,
MessageHandler,
CommandHandler,
filters
)

from handlers.messages import mensaje
from handlers.commands import start, help, reset, ping
from config import TOKEN

app=Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("help",help))
app.add_handler(CommandHandler("reset",reset))
app.add_handler(CommandHandler("ping", ping))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        mensaje
    )
)

print("Bot iniciado")

app.run_polling()
