from telegram.ext import (
Application,
MessageHandler,
CommandHandler,
filters
)

from handlers.messages import mensaje
from handlers.commands import start, help, reset, ping, config, stats, about
from config import TOKEN
from handlers.images import imagen
from utils.logger import logger

app=Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("help",help))
app.add_handler(CommandHandler("reset",reset))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("config", config))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("about", about))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        mensaje
    )
)

app.add_handler(
    MessageHandler(
        filters.PHOTO,
        imagen
    )
)


async def error_handler(update, context):

    logger.exception(context.error)

app.add_error_handler(error_handler)
print("Bot iniciado")

app.run_polling()
