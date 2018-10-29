# to create a standalone executable, use pyinstaller
# pyinstaller --onefile --window db_frontend.py
# need to provide database file as well

#imports
from tkinter import *
import db_backend


# callbacks
def get_selected_row(event) :
    try:
        global selected_tuple
        index=lb1.curselection()[0]
        selected_tuple=lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError :
        pass

def view_command() :
    lb1.delete(0,END)
    for row in db_backend.view() :
        lb1.insert(END,row)

def search_command() :
    lb1.delete(0,END)
    for row in db_backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()) :
        lb1.insert(END,row)

def addentry_command():
    db_backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    lb1.delete(0,END)
    lb1.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))

def update_command():
    db_backend.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])

def delete_command():
    db_backend.delete(selected_tuple[0])
    view_command()


# create window
window=Tk()
window.wm_title("Bookstore")

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

# initialize and place widgets
l1=Label(window, text="Title")
l1.grid(row=0,column=0)
l2=Label(window, text="Author")
l2.grid(row=0,column=2)
l3=Label(window, text="Year")
l3.grid(row=1,column=0)
l4=Label(window, text="ISBN")
l4.grid(row=1,column=2)

title_value=StringVar()
e1=Entry(window,textvariable=title_value)
e1.grid(row=0,column=1)
author_value=StringVar()
e2=Entry(window,textvariable=author_value)
e2.grid(row=0,column=3)
year_value=StringVar()
e3=Entry(window,textvariable=year_value)
e3.grid(row=1,column=1)
isbn_value=StringVar()
e4=Entry(window,textvariable=isbn_value)
e4.grid(row=1,column=3)

lb1=Listbox(window,height=8, width=35)
lb1.grid(row=2,column=0,rowspan=8,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10, sticky='ns')

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

lb1.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(window, text="View All", width=12,command=view_command)
b1.grid(row=2,column=3,columnspan=2)
b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3,column=3,columnspan=2)
b3=Button(window, text="Add Entry", width=12, command=addentry_command)
b3.grid(row=4,column=3,columnspan=2)
b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5,column=3,columnspan=2)
b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6,column=3,columnspan=2)
b6=Button(window, text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3,columnspan=2)


# keeps the window open
window.mainloop()
