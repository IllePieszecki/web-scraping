from pymongo import MongoClient

# Conexión al servidor local
client = MongoClient("mongodb://127.0.0.1:27017/")

# Selecciona la base y colección
db = client["twice_calendar"]
collection = db["twice_events"]

# Documento ejemplo
eventos = [
    {
        "_id": "twice-2025-09-11-album-release",
        "date": "2025-09-11",
        "time": "13:00",
        "title": "LIL FANTASY vol.1 Album Release"
    },
    {
        "_id": "twice-2025-09-11-mv-release",
        "date": "2025-09-11",
        "time": "13:00",
        "title": "SHOOT (Firecracker) MV Release"
    }
]

collection.insert_many(eventos)
print("Varios eventos insertados.")


# Insertar
# collection.insert_one(evento)

print("Evento insertado correctamente.")
