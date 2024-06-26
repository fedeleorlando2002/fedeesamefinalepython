from pymongo import MongoClient
from faker import Faker
from random import randint

# Connessione al client MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.libreria  # Database 'libreria'
collection = db.libri  # Collezione 'libri'

# Creazione di istanze Faker per dati casuali
fake = Faker()

# Funzione per generare dati casuali per un libro
def generate_book():
    return {
        'titolo': fake.catch_phrase(),
        'autore': fake.name(),
        'prezzo': randint(10, 100),
        'categoria': fake.word()
    }

# Generazione di dati casuali e inserimento nella collezione
def seed_database(num_entries):
    for _ in range(num_entries):
        book_data = generate_book()
        collection.insert_one(book_data)

if __name__ == '__main__':
    num_entries = 10  # Numero di voci da inserire nel database
    seed_database(num_entries)
    print(f"{num_entries} voci inserite nel database 'libreria' nella collezione 'libri'")
