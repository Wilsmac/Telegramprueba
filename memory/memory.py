memoria = {}

def obtener(chat_id):

    if chat_id not in memoria:
        memoria[chat_id] = []

    return memoria[chat_id]
