from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

ekran = tk.Tk()
ekran.title("książka telefoniczna")
ekran.geometry("800x600")

class Kontakt:
    def __init__(self, imie, nazwisko, nr_tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_tel = nr_tel

    def __repr__(self):
        return f' {self.imie} {self.nazwisko} {self.nr_tel}'

    def ustaw_imie(self, imie):
        self.imie = imie

# def tworzenie_nowego_kontaktu():
#     window = tk.Toplevel()
#     label1 = Label(window, text="Podaj imie :")
#     label1.grid(row=0, column=0)
#     okno = Entry(window)
#
#     def zapisz(self):
#         zawartosc = okno.get()
#         kontakty.append(zawartosc)
#         print(kontakty)
#         kontakty_var.set(kontakty)
#
#     okno.grid(row=0, column=1)
#     okno.bind('<Return>', zapisz)
# mainframe = ttk.Frame(ekran, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# ekran.columnconfigure(0, weight=1)
# ekran.rowconfigure(0, weight=1)

kontakty = []
kontakty_var = tk.StringVar(value=kontakty)
lista_kontaktow = Listbox(ekran, listvariable=kontakty_var, height=30, width=132, selectmode='extended')
lista_kontaktow.grid(column=0, row=0, sticky='nwes')

def tworzenie_nowego_kontaktu():
    window = tk.Toplevel()
    okno_imie = input_kontakt(window, "podaj imie", 0)
    okno_nazwisko = input_kontakt(window, "podaj nazwisko", 1)
    okno_nr = input_kontakt(window, "podaj nr tel", 2)


    def action():
        kontakt = Kontakt(okno_imie.get(), okno_nazwisko.get(), okno_nr.get())
        kontakty.append(kontakt)
        kontakty_var.set(kontakty)
        print(kontakty)
        window.destroy()

    button_close = tk.Button(window, text="Close", command=action)
    button_close.grid(row=3, column=0, sticky='we')

def input_kontakt(window, tekst, row):
    label1 = Label(window, text=tekst)
    label1.grid(row=row, column=0)
    okno = Entry(window)
    okno.grid(column=2, row=row, sticky=(N, W, E, S))
    return okno



nowy_kontakt = tk.Button(ekran, text="dodaj nowy kontakt", command=tworzenie_nowego_kontaktu, height=3, width=20, bg='#567', fg='White')
nowy_kontakt.grid(column=0, row=3, sticky=(N, W, E, S))
ekran.mainloop()