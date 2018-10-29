# to create a standalone executable, use pyinstaller
# pyinstaller --onefile --window db_frontend.py
# need to provide database file as well

#imports
from tkinter import *
from db_backendOOP import Database


class Window:

    def __init__(self,window) :
        self.database=Database(r"D:\dev\practice_workspace\app5_DbGUI\resources\books.db")

        # create window

        window.wm_title("Bookstore")

        # initialize and place widgets
        self.l1=Label(window, text="Title")
        self.l1.grid(row=0,column=0)
        self.l2=Label(window, text="Author")
        self.l2.grid(row=0,column=2)
        self.l3=Label(window, text="Year")
        self.l3.grid(row=1,column=0)
        self.l4=Label(window, text="ISBN")
        self.l4.grid(row=1,column=2)

        self.title_value=StringVar()
        self.e1=Entry(window,textvariable=self.title_value)
        self.e1.grid(row=0,column=1)
        self.author_value=StringVar()
        self.e2=Entry(window,textvariable=self.author_value)
        self.e2.grid(row=0,column=3)
        self.year_value=StringVar()
        self.e3=Entry(window,textvariable=self.year_value)
        self.e3.grid(row=1,column=1)
        self.isbn_value=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_value)
        self.e4.grid(row=1,column=3)

        self.lb1=Listbox(window,height=8, width=35)
        self.lb1.grid(row=2,column=0,rowspan=8,columnspan=2)

        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2,column=2,rowspan=10, sticky='ns')

        self.lb1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.lb1.yview)

        self.lb1.bind("<<ListboxSelect>>",self.get_selected_row)

        b1=Button(window, text="View All", width=12,command=self.view_command)
        b1.grid(row=2,column=3,columnspan=2)
        b2=Button(window, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3,column=3,columnspan=2)
        b3=Button(window, text="Add Entry", width=12, command=self.addentry_command)
        b3.grid(row=4,column=3,columnspan=2)
        b4=Button(window, text="Update", width=12, command=self.update_command)
        b4.grid(row=5,column=3,columnspan=2)
        b5=Button(window, text="Delete", width=12, command=self.delete_command)
        b5.grid(row=6,column=3,columnspan=2)
        b6=Button(window, text="Close", width=12,command=window.destroy)
        b6.grid(row=7,column=3,columnspan=2)

    # callbacks
    def get_selected_row(self, event) :
        try:
            index=self.lb1.curselection()[0]
            self.selected_tuple=self.lb1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError :
            pass

    def view_command(self) :
        self.lb1.delete(0,END)
        for row in self.database.view() :
            self.lb1.insert(END,row)

    def search_command(self) :
        self.lb1.delete(0,END)
        for row in self.database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()) :
            self.lb1.insert(END,row)

    def addentry_command(self):
        self.database.insert(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.lb1.delete(0,END)
        self.lb1.insert(END,(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))

    def update_command(self):
        self.database.update(self.selected_tuple[0],self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        print(self.selected_tuple[0],self.selected_tuple[1],self.selected_tuple[2],self.selected_tuple[3],self.selected_tuple[4])

    def delete_command(self):
        self.database.delete(self.selected_tuple[0])
        self.view_command()






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



window=Tk()
Window(window)
# keeps the window open
window.mainloop()
