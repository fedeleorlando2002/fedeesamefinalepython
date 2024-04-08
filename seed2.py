# from pymongo import MongoClient
# from faker import Faker
# from random import randint

# # Connessione al client MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client.libreria  # Database 'libreria'
# collection = db.clienti  # Collezione 'clienti'

# # Creazione di istanze Faker per dati casuali
# fake = Faker()

# # Funzione per generare dati casuali per un cliente
# def generate_customer():
#     return {
#         'nome': fake.first_name(),
#         'cognome': fake.last_name(),
#         'eta': randint(18, 90),
#         'email': fake.email(),
#         'telefono': fake.phone_number()
#     }

# # Generazione di dati casuali e inserimento nella collezione
# def seed_database(num_entries):
#     for _ in range(num_entries):
#         customer_data = generate_customer()
#         collection.insert_one(customer_data)

# if __name__ == '__main__':
#     num_entries = 10  # Numero di voci da inserire nel database
#     seed_database(num_entries)
#     print(f"{num_entries} voci inserite nel database 'libreria' nella collezione 'clienti'")


from pymongo import MongoClient
from faker import Faker
from datetime import datetime, timedelta
import random

# Connessione al client MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.libreria  # Database 'libreria'
collection = db.clienti  # Collezione 'clienti'

# Creazione di un'istanza Faker per dati casuali
fake = Faker()

# Funzione per generare una data di nascita casuale
def generate_birthdate():
    # Genera una data compresa tra 18 e 90 anni fa
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return birthdate

# Funzione per generare dati casuali per un cliente
def generate_customer():
    birthdate = generate_birthdate()  # Genera una data di nascita
    return {
        'nome': fake.first_name(),
        'cognome': fake.last_name(),
        'eta': birthdate.strftime("%Y-%m-%d"),  # Converti la data in una stringa
        'email': fake.email(),
        'telefono': fake.phone_number()
    }

# Generazione di dati casuali e inserimento nella collezione
def seed_database(num_entries):
    for _ in range(num_entries):
        customer_data = generate_customer()
        collection.insert_one(customer_data)

if __name__ == '__main__':
    num_entries = 15  # Numero di voci da inserire nel database
    seed_database(num_entries)
    print(f"{num_entries} voci inserite nel database 'libreria' nella collezione 'clienti'")
