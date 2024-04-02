class Author:
    def __init__(self, id, name, bio):
        self.id = id
        self.name = name
        self.bio = bio

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte meno autora: ")
        meno = input()
        print("Vlozte bio autora: ")
        bio = input()
        cursor.execute("INSERT INTO authors (name, bio) VALUES (%s, %s)", (meno, bio))

    @staticmethod
    def zobraz_autora(cursor):
        cursor.execute("SELECT * FROM authors")
        autori = cursor.fetchall()
        for autor in autori:
            print(f"{autor[0]}. {autor[1]}")
        print("\n")




    def __str__(self):
        return f"---AUTHOR---\nID Autora: {self.id}\nMeno: {self.name}\nBio: {self.bio}"
