#! python3
# This is a VERY rough first attempt to GUI!

from tkinter import *

def show_entry_fields():
    e5.delete(0,END)
    fv = float(e1.get())
    iyr = float(e2.get())/100
    y = float(e3.get())
    pyr = int(e4.get())
    pmt = fv/((1+iyr/pyr)*(((1+iyr/pyr)**(y*pyr)-1))/(iyr/pyr))
    pmt = round(pmt, 2)
    #TODO: what is first argument 'string' in .insert?
    e5.insert(1,pmt) 



master = Tk()
info = 'Ile odkładać, aby po latach otrzymać określoną kwotę'
Label(master, text=info).grid(row=0)
Label(master, text='Przyszła kwota').grid(row=1)
Label(master, text='Roczna stopa procentowa').grid(row=2)
Label(master, text='Lata odkładania').grid(row=3)
Label(master, text='Ilość kapitalizacji').grid(row=4)
Label(master, text='Suma do wpłacania').grid(row=5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=6, column=1, sticky=W, pady=4)

mainloop()
