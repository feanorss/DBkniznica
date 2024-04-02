class Genre:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte meno zanru: ")
        meno = input()
        print("Vlozte popis: ")
        description = input()
        cursor.execute("INSERT INTO genres (name, description) VALUES (%s, %s)", (meno, description))

    @staticmethod
    def zobraz_zaner(cursor):
        cursor.execute("SELECT * FROM genres")
        genres = cursor.fetchall()
        for genre in genres:
            print(f"{genre[0]}. {genre[1]}")
        print("\n")

    def __str__(self):
        return f"---GENRES---\nID Genre: {self.id}\nMeno: {self.name}\nDescription: {self.Description}"