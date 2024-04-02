import psycopg2
from author import Author
from genre import Genre
from Book import Book

conn = psycopg2.connect(
    dbname = "bphzurc4badokyq3ezig",
    user = "ucrksoznquj3b71nfqcv",
    password = "2YKt1zZxmkqsYgV41W3260QJNXRTn6",
    host = "bphzurc4badokyq3ezig-postgresql.services.clever-cloud.com",
    port = "50013"
)

cursor = conn.cursor()

def vypis_menu():
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")

def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
        elif choice == "3":
            Author.zobraz_autora(cursor)
            authorID = input("ID Authora: ")
            Genre.zobraz_zaner(cursor)
            genreID = input("ID zanru: ")
            Book.vloz_do_db(cursor, authorID, genreID)
            conn.commit()
        else:
            print("Neplatny vstup")

aplikacia()