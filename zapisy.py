import json

class Kontakt:
    def __init__(self, imie, nazwisko, nr_tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_tel = nr_tel

    def __repr__(self):
        return f' {self.imie} {self.nazwisko} {self.nr_tel}'

kontakt = Kontakt("Maja", "Lachowicz", "123")
print(kontakt.__dict__)
plik = "zap_k.json"
with open(plik, "w", encoding="utf-8") as zapisane_kontakty:
    json.dump([kontakt.__dict__, kontakt.__dict__], zapisane_kontakty)

