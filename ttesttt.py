print("napis")

osoba = ["napis1", 123]
print(osoba)

krotka = ("napis1", "napis2")
print(krotka)

print(krotka[0])
INDEX_OZNACZAJACY_IMIE = 0
print(osoba[INDEX_OZNACZAJACY_IMIE])


class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __repr__(self):
        return f'Osoba {self.imie} {self.nazwisko} {self.wiek}'


qwe = Osoba("Maja","Lachowicz", 23)

osoby = [qwe,qwe,qwe]
print(osoby)
print(qwe.imie)
