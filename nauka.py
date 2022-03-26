# # from tkinter import Tk, Label, Button
# #
# # ekran = Tk()
# # ekran.title("książka telefoniczna")
# # ekran.geometry("800x600")
# #
# # napis = Label(ekran, text="Książka telefoniczna", font=30, fg="blue")
# # napis.pack()
# #
# # clicks = 0
# #
# #
# # def click_action(button):
# #     global clicks
# #     clicks += 1
# #     button.config(text=f"Wow! x {clicks}")
# #
# #
# # przycisk = Button(ekran, text="dodaj nowy kontakt", width=20)
# # przycisk.pack()
# #
# # przycisk.config(command=lambda: click_action(przycisk))
# #
# # lista = ["Maja", "Kasper", "Lucyfer", "Bonifacy"]
# # for i in lista:
# #     kontakt = Label(ekran, text=i, font=30, fg="black")
# #     kontakt.pack()
# #
# # ekran.mainloop()
#
# import tkinter as tk
# from tkinter.messagebox import showinfo
#
# # --- functions ---
#
# def popup_window():
#     window = tk.Toplevel()
#
#     label = tk.Label(window, text="Hello World!")
#     label.pack(fill='x', padx=50, pady=5)
#
#     button_close = tk.Button(window, text="Close", command=window.destroy)
#     button_close.pack(fill='x')
#
# def popup_showinfo():
#     showinfo("ShowInfo", "Hello World!")
#
# # --- main ---
#
# root = tk.Tk()
#
# button_bonus = tk.Button(root, text="Window", command=popup_window)
# button_bonus.pack(fill='x')
#
# button_showinfo = tk.Button(root, text="ShowInfo", command=popup_showinfo)
# button_showinfo.pack(fill='x')
#
# button_close = tk.Button(root, text="Close", command=root.destroy)
# button_close.pack(fill='x')
#
# root.mainloop()
#
#
#


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Listbox')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    selectmode='extended')

listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

# handle event
def items_selected(event):
    """ handle item selected event
    """
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(
        title='Information',
        message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()

#
# from tkinter import *
# import tkinter as tk
#
# ekran = tk.Tk()
# ekran.title("książka telefoniczna")
# ekran.geometry("800x600")
#
# def okno_kontaktu():
#     window = tk.Toplevel()
#     elementy_kontaktu = ["IMIE", "NAZWISKO", "NR TELEFONU"]
#     for i in elementy_kontaktu:
#         label = tk.Label(window, text=i)
#         label.pack(fill='x', padx=100, pady=5)
#
#     button_close = tk.Button(window, text="Close", command=window.destroy)
#     button_close.pack(fill='x')
#
# def tworzenie_nowego_kontaktu():
#     window = tk.Toplevel()
#     label1 = Label(window, text="Podaj imie :")
#     label1.grid(row=0, column=0)
#     okno = Entry(window)
#
#     def wydrukuj(self):
#         zawartosc = okno.get()
#         imiona.append(zawartosc)
#         print(imiona)
#
#     okno.grid(row=0, column=1)
#     okno.bind('<Return>', wydrukuj)
#     okno.bind('<Tab>', wydrukuj)
#     button_close = tk.Button(window, text="Close", command=window.destroy)
#     button_close.grid(row=1, column=0)
#
# lista_kontaktow = ["Maja", "Kasper"]
# a = 20
# for i in lista_kontaktow:
#     kontakt = tk.Button(ekran, text=i, command=okno_kontaktu, height=2, width=20)
#     kontakt.place(x=20, y=a)
#     a += 50
#
#
# nowy_kontakt = tk.Button(ekran, text="dodaj nowy kontakt", command=tworzenie_nowego_kontaktu, height=3, width=20, bg='#567', fg='White')
# nowy_kontakt.place(x=20, y=500)
#
# imiona = []
#
#
# # definiowanie funkcji nazwa- wydrukuj
#
#
#
#
#
# ekran.mainloop()