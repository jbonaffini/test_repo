import sqlite3

# Connect to DB
# Create cursor object
# Write SQL query
# Commit changes to DB
# close DB connection

def create_table() :
    conn=sqlite3.connect(r".\DB_practice\lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert (item, quantity, price):
    conn=sqlite3.connect(r".\DB_practice\lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view() :
    conn=sqlite3.connect(r".\DB_practice\lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item) :
    conn=sqlite3.connect(r".\DB_practice\lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,)) # need , here
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn=sqlite3.connect(r".\DB_practice\lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


#create_table()
insert("Wine Glass", 10, 6.0)
print(view())
update(11,6.0,"Wine Glass")
print(view())
delete("Wine Glass")
print(view())
