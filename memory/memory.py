from database.database import cargar

cache={}

def obtener(chat_id):

    if chat_id not in cache:
        cache[chat_id]=cargar(chat_id)

    return cache[chat_id]
