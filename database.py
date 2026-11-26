
import sqlite3

# Database connection
conn = sqlite3.connect("movieDB.sqlite3")

cursor = conn.cursor()

# Movie Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Movie(
    movie_id INTEGER PRIMARY KEY,
    genre TEXT,
    time TEXT
)
""")

# Hall Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Hall(
    hall_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES Movie(movie_id)
)
""")

# Multiplex Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Multiplex(
    multiplex_id INTEGER,
    movie_id INTEGER,
    hall_id INTEGER,
    PRIMARY KEY(multiplex_id, hall_id),
    FOREIGN KEY(movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY(hall_id) REFERENCES Hall(hall_id)
)
""")

conn.commit()
conn.close()

print("Database and Tables Created Successfully!")



import sqlite3

conn = sqlite3.connect("movieDB.sqlite3")
cursor = conn.cursor()

# Movie Data
cursor.executemany("""
INSERT OR IGNORE INTO Movie(movie_id, genre, time)
VALUES (?, ?, ?)
""", [
    (1, "Action", "10:00 AM"),
    (2, "Comedy", "1:00 PM"),
    (3, "Horror", "4:00 PM"),
    (4, "Romance", "7:00 PM"),
    (5, "Thriller", "9:00 PM")
])

# Hall Data
cursor.executemany("""
INSERT OR IGNORE INTO Hall(hall_id, movie_id)
VALUES (?, ?)
""", [
    (101, 1),
    (102, 2),
    (103, 3),
    (104, 4),
    (105, 5)
])

# Multiplex Data
cursor.executemany("""
INSERT OR IGNORE INTO Multiplex(multiplex_id, movie_id, hall_id)
VALUES (?, ?, ?)
""", [
    (1, 1, 101),
    (1, 2, 102),
    (2, 3, 103),
    (2, 4, 104),
    (3, 5, 105)
])

conn.commit()
conn.close()

print("Sample Data Inserted Successfully!")



import sqlite3

conn = sqlite3.connect("movieDB.sqlite3")

cursor = conn.cursor()

query = """
SELECT
    Movie.movie_id,
    Movie.genre,
    Movie.time,
    Hall.hall_id,
    Multiplex.multiplex_id

FROM Movie

JOIN Hall
ON Movie.movie_id = Hall.movie_id

JOIN Multiplex
ON Hall.hall_id = Multiplex.hall_id
"""

cursor.execute(query)

data = cursor.fetchall()

for row in data:
    print(row)

conn.close()
