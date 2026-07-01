import sqlite3

conexion = sqlite3.connect("chatbot.db", check_same_thread=False)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memoria(
    chat_id INTEGER,
    role TEXT,
    content TEXT
)
""")

conexion.commit()

def guardar(chat_id, role, content):
    cursor.execute(
        "INSERT INTO memoria VALUES (?,?,?)",
        (chat_id, role, content)
    )
    conexion.commit()

def cargar(chat_id):

    cursor.execute(
        "SELECT role, content FROM memoria WHERE chat_id=?",
        (chat_id,)
    )

    datos = cursor.fetchall()

    historial=[]

    for rol,texto in datos:

        historial.append({
            "role":rol,
            "content":texto
        })

    return historial

def borrar(chat_id):

    cursor.execute(
        "DELETE FROM memoria WHERE chat_id=?",
        (chat_id,)
    )

    conexion.commit()
