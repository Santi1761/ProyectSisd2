from pymongo import MongoClient
from django.conf import settings

def check_mongo_connection():
    try:
        client = MongoClient(settings.DATABASES['mongodb']['CLIENT']['host'])
        db = client.get_database('tech_services_db')
        print("Conexión exitosa a MongoDB:", db.name)
    except Exception as e:
        print("Error conectando a MongoDB:", e)

check_mongo_connection()
