import sqlite3
def db():
    return sqlite3.connect("movies.db")

def image():
    conn=db()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ratings(
                   userId TEXT,
                   movieId TEXT,
                   rating REAL
                   )
"""
    )
    conn.commit()
    conn.close()

def add_rating(userId, movieId, rating):
    conn=db()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO raiting VALUES (?, ?, ?)", (userId, movieId, rating))
    conn.commit()
    conn.close()    

def your_rating(userId):
    conn=db()
    cursor=conn.cursor()
    cursor.execute("SELECT movieId, rating FROM ratings WHERE userId = ?", (userId))
    wynik=cursor.fetchall()
    conn.close()
    return wynik