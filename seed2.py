from pymongo import MongoClient
from faker import Faker
from random import randint

# Connessione al client MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.libreria  # Database 'libreria'
collection = db.clienti  # Collezione 'clienti'

# Creazione di istanze Faker per dati casuali
fake = Faker()

# Funzione per generare dati casuali per un cliente
def generate_customer():
    return {
        'nome': fake.first_name(),
        'cognome': fake.last_name(),
        'eta': randint(18, 90),
        'email': fake.email(),
        'telefono': fake.phone_number()
    }

# Generazione di dati casuali e inserimento nella collezione
def seed_database(num_entries):
    for _ in range(num_entries):
        customer_data = generate_customer()
        collection.insert_one(customer_data)

if __name__ == '__main__':
    num_entries = 10  # Numero di voci da inserire nel database
    seed_database(num_entries)
    print(f"{num_entries} voci inserite nel database 'libreria' nella collezione 'clienti'")

