from tkinter import *

# initalize the window
window=Tk()

def km_to_mi():
    # conversion factor
    conv_fac = 0.621371
    miles=float(e1_value.get())/conv_fac
    t1.insert(END,miles)
    print("Success")

def convert_command1() :
    kg_to_grams()
    kg_to_lbs()
    kg_to_oz()

def kg_to_grams() :
    # conversion factor
    conv_fac = 1000
    grams=float(e1_value.get())*conv_fac
    t1.insert(END,grams)

def kg_to_lbs() :
    # conversion factor
    conv_fac = 2.20462
    lbs=float(e1_value.get())*conv_fac
    t2.insert(END,lbs)


def kg_to_oz() :
    # conversion factor
    conv_fac = 35.274
    oz=float(e1_value.get())*conv_fac
    t3.insert(END,oz)

# initialize and place widgets
l1=Label(window, text="Kg")
l1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window, text="Convert",command=convert_command1)
b1.grid(row=0,column=2)

t1=Text(window,height=1, width=20)
t1.grid(row=1,column=0,columnspan=1)

t2=Text(window,height=1, width=20)
t2.grid(row=1,column=1,columnspan=1)

t3=Text(window,height=1, width=20)
t3.grid(row=1,column=2,columnspan=1)

#callbacks


# keeps the window open
window.mainloop()
