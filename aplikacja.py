from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo

ekran = tk.Tk()
ekran.title("książka telefoniczna")
ekran.geometry("800x600")


def okno_kontaktu():
    window = tk.Toplevel()
    elementy_kontaktu = ["IMIE", "NAZWISKO", "NR TELEFONU"]
    for i in elementy_kontaktu:
        label = tk.Label(window, text=i)
        label.pack(fill='x', padx=100, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')

def tworzenie_nowego_kontaktu():
    window = tk.Toplevel()
    input_kontakt(window, "podaj imie", 0, lambda z: imiona.append(z))
    input_kontakt(window, "podaj nazwisko", 1, lambda z: nazwiska.append(z))
    input_kontakt(window, "podaj nr tel", 2, lambda z: nr_tel.append(z))
    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.grid(row=3, column=0, sticky='we')

def input_kontakt(window, tekst, row, x):
    label1 = Label(window, text=tekst)
    label1.grid(row=row, column=0)
    okno = Entry(window)

    def wydrukuj(self):
        zawartosc = okno.get()
        x(zawartosc)

    okno.grid(row=row, column=1)
    okno.bind('<Return>', wydrukuj)
    okno.bind('<Tab>', wydrukuj)


imiona = []
nazwiska = []
nr_tel = []

# lista_kontaktow = ["Maja", "Kasper"]
# a = 20
# for i in lista_kontaktow:
#     kontakt = tk.Button(ekran, text=i, command=okno_kontaktu, height=2, width=20)
#     kontakt.place(x=20, y=a)
#     a += 50

kontakty = ["Maja", "Kasper", "Lucyfer", "Markiz", "Bonifacy"]
kontakty_var = tk.StringVar(value=kontakty)
lista_kontaktow = Listbox(ekran, listvariable=kontakty_var, height=30, width=132, selectmode='extended')
lista_kontaktow.grid(column=0, row=0, sticky='nwes')



# nowy_kontakt = tk.Button(ekran, text="dodaj nowy kontakt", command=tworzenie_nowego_kontaktu, height=3, width=20, bg='#567', fg='White')
# nowy_kontakt.place(x=20, y=500)





ekran.mainloop()

# lista w listbox
# dodaj kontakt, wpisze sie do tej listy