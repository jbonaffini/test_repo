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

class Database :

    def __init__(self, db) :
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def __del__(self) :
        self.conn.close()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def search(self, title="", author="", year="", isbn="") :
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete(self, id) :
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, title="", author="", year="", isbn="") :
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()


# runs when backend is imported to frontend python file
#connect()
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
