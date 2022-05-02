from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json


ekran = tk.Tk()
ekran.title("książka telefoniczna")
# ekran.geometry("600x800")
frame = ttk.Frame(ekran)


class Kontakt:
    def __init__(self, imie, nazwisko, nr_tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_tel = nr_tel

    def __repr__(self):
        return f' {self.imie} {self.nazwisko} {self.nr_tel}'

    def ustaw_imie(self, imie):
        self.imie = imie

try:
    f = open('zap_k.json', "r")
    kontakty_json = json.loads(f.read())
except FileNotFoundError:
    kontakty_json = []
    print("nie znaleziono pliku. lista kontaktów jest pusta")


def from_json(json_kontakt):
    return Kontakt(json_kontakt["imie"], json_kontakt["nazwisko"], json_kontakt["nr_tel"])
lista_kontaktow = []

for json_kontakt in kontakty_json:
    kontakt = from_json(json_kontakt)
    lista_kontaktow.append(kontakt)


kontakty_var = tk.StringVar(value=lista_kontaktow)
widok_kontaktow = Listbox(frame, listvariable=kontakty_var, selectmode='extended')
# scrollbar = tk.Scrollbar(ekran, orient='vertical', command=widok_kontaktow.yview)
# scrollbar.grid(row=0, column=3, sticky='nse')
# widok_kontaktow.config(yscrollcommand=scrollbar.set)

def tworzenie_nowego_kontaktu():
    window = tk.Toplevel()
    okno_imie = input_kontakt(window, "podaj imie", 0)
    okno_nazwisko = input_kontakt(window, "podaj nazwisko", 1)
    okno_nr = input_kontakt(window, "podaj nr tel", 2)

    def action():
        # nr_zaznaczonej_linii = widok_kontaktow.curselection()
        # print(nr_zaznaczonej_linii)
        kontakt = Kontakt(okno_imie.get(), okno_nazwisko.get(), okno_nr.get())
        lista_kontaktow.append(kontakt)
        zapiszListeKontaktow(lista_kontaktow)
        kontakty_var.set(lista_kontaktow)
        print(kontakty_json)
        window.destroy()

    button_zapisz = tk.Button(window, text="Zapisz", command=action)
    button_zapisz.grid(row=3, column=0, sticky='we')


def zapiszListeKontaktow(lista_kontaktow):
    plik = "zap_k.json"
    lista_map = []
    for k in lista_kontaktow:
        k_json = k.__dict__
        lista_map.append(k_json)
    with open(plik, "w", encoding="utf-8") as uchwyt_do_pliku:
        caly_json = json.dumps(lista_map)
        uchwyt_do_pliku.write(caly_json)

def input_kontakt(window, tekst, row):
    label1 = Label(window, text=tekst)
    label1.grid(row=row, column=0)
    okno = Entry(window)
    okno.grid(column=2, row=row, sticky=(N, W, E, S))
    okno.focus_set()
    return okno


def usuwanie_kontaktu():
    print("do usuniecia")
    index = widok_kontaktow.curselection()
    if index:
        del lista_kontaktow[index[0]]
        zapiszListeKontaktow(lista_kontaktow)
        kontakty_var.set(lista_kontaktow)
        print(lista_kontaktow[index[0]])



def input_do_edycji(window, tekst, row, x):
    label1 = Label(window, text=tekst)
    label1.grid(row=row, column=0)
    okno = Entry(window)
    okno.insert(0, x)
    okno.grid(column=2, row=row, sticky=(N, W, E, S))
    okno.focus_set()
    return okno

def okno_do_edycji():
    window = tk.Toplevel()
    index = widok_kontaktow.curselection()
    wyb_kontakt = lista_kontaktow[index[0]]

    okno_imie = input_do_edycji(window, "podaj imie", 0, wyb_kontakt.imie)
    okno_nazwisko = input_do_edycji(window, "podaj nazwisko", 1, wyb_kontakt.nazwisko)
    okno_nr = input_do_edycji(window, "podaj nr tel", 2, wyb_kontakt.nr_tel)
    def action():
        kontakt = Kontakt(okno_imie.get(), okno_nazwisko.get(), okno_nr.get())
        lista_kontaktow.append(kontakt)
        zapiszListeKontaktow(lista_kontaktow)
        kontakty_var.set(lista_kontaktow)
        print(kontakty_json)
        window.destroy()

    button_zapisz = tk.Button(window, text="Zapisz", command=action)
    button_zapisz.grid(row=3, column=0, sticky='we')

def edytowanie_kontaktu():
    index = widok_kontaktow.curselection()
    if index:
        okno_do_edycji()




nowy_kontakt = tk.Button(frame, text="dodaj nowy kontakt", command=tworzenie_nowego_kontaktu, bg='#567', fg='White')

edytuj_kontakt = tk.Button(frame, text="edytuj kontakt", command=edytowanie_kontaktu, bg='#567', fg='White')

usun_kontakt = tk.Button(frame, text="usuń kontakt", command=usuwanie_kontaktu, bg='#567', fg='White')



frame.grid(column=0, row=0)
nowy_kontakt.grid(row=2, column=0)
edytuj_kontakt.grid(row=2, column=1)
usun_kontakt.grid(row=2, column=2)
widok_kontaktow.grid(row=0, column=0, pady="5 20", columnspan=2, sticky="nwes")

ekran.mainloop()
