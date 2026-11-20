import sqlite3

connection = sqlite3.connect('Animals.sl3')

cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS Animals (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL
    );"""

cursor.execute(sql)

sql = """
    INSERT INTO Animals (name, type) VALUES
    ('Лев', 'Ссавець'),
    ('Крокодил', 'Плазун'),
    ('Орел', 'Птах'),
    ('Морська черепаха', 'Плазун'),
    ('Мавпа', 'Ссавець')
"""

cursor.execute(sql)

sql = """
    UPDATE Animals
    SET name = 'Сокіл'
    WHERE name = 'Орел'
"""

cursor.execute(sql)

sql = "SELECT * FROM Animals WHERE type = 'Ссавець'"
cursor.execute(sql)

animals = cursor.fetchall()

print("Звірі типу Ссавець:")
for animal in animals:
    id, name, type = animal
    print(f"{id} | {name} | {type}")

sql = "SELECT * FROM Animals"
cursor.execute(sql)

animals = cursor.fetchall()

print("Всі звірі:")
for animal in animals:
    id, name, type = animal
    print(f"{id} | {name} | {type}")

connection.commit()

connection.close()
