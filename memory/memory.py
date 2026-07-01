from database.database import cargar

MAX_HISTORY = 20

cache = {}

def obtener(chat_id):

    if chat_id not in cache:
        cache[chat_id] = cargar(chat_id)

    return cache[chat_id]

def agregar(chat_id, role, content):

    historial = obtener(chat_id)

    historial.append({
        "role": role,
        "content": content
    })

    if len(historial) > MAX_HISTORY:
        historial.pop(0)

    return historial
