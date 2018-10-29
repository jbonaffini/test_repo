import sqlite3

"""
Program stores the following information
Title, Author, Year, ISBN

User Can:
View all records
Search an Entry
Add an Entry
Update an Entry
Delete
Close
"""


def connect():
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="", author="", year="", isbn="") :
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id) :
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title="", author="", year="", isbn="") :
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()


# runs when backend is imported to frontend python file
connect()
#insert("Hola", "Juan Smith", 2000, 112312312312)
#print(view())
#print(search(author="Juan Smith"))
#update(6,"Hola2", "Juan Smith", 2000, 112312312312)
#print(search(author="Juan Smith"))




def template():
    conn=sqlite3.connect(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")
    cur=conn.cursor()
    cur.execute("")
    conn.commit()
    conn.close()
