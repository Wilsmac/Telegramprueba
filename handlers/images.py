from telegram import Update
from telegram.ext import ContextTypes

async def imagen(update: Update, context: ContextTypes.DEFAULT_TYPE):

    foto = update.message.photo[-1]

    archivo = await context.bot.get_file(foto.file_id)

    await archivo.download_to_drive("imagen.jpg")

    await update.message.reply_text(
        "📷 Imagen recibida correctamente."
    )
