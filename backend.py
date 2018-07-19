import sqlite3

def connect():
    conn = sqlite3.connect("Database.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS "
                "Book_dir (id integer PRIMARY KEY, "
                "Title text, "
                "Author text, "
                "Year integer, "
                "ISBN integer)")
    conn.commit()
    conn.close()


def insert(Title, Author, Year, ISBN):
    
    conn = sqlite3.connect("Database.db")
    curs = conn.cursor()
    curs.execute("INSERT INTO Book_dir "
                "VALUES (NULL, ?, ?, ?, ?)", (Title, Author, Year, ISBN))
    conn.commit()
    conn.close()

def view():
    
    conn = sqlite3.connect("Database.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM Book_dir")
    rows = curs.fetchall()
    conn.close()
    return rows

def update(id, Title, Author, Year, ISBN):
    
    conn = sqlite3.connect("Database.db")
    curs = conn.cursor()
    curs.execute("UPDATE Book_dir "
                "SET Title = ?, "
                "Author = ?, "
                "Year = ?, "
                "ISBN = ? "
                "WHERE id = ?", 
                (Title, Author, Year, ISBN, id))
    conn.commit()
    conn.close()


def delete(id):
    
    conn = sqlite3.connect("Database.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM Book_dir "
                "WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def search(Title = "", Author = "", Year = "", ISBN = ""):
    
    conn = sqlite3.connect("Database.db")
    curs = conn.cursor()
    curs.execute("SELECT * "
                "FROM Book_dir "
                "WHERE Title = ? OR Author = ? OR Year = ? OR ISBN = ?", 
                (Title, Author, Year, ISBN))
    rows = curs.fetchall()
    conn.close()
    return rows

connect()
