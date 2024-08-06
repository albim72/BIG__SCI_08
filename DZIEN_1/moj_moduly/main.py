# import dane
# import dane as dn

from dane import nrfilii as nf
from dane import book as bk

from moje_funkcje.kolekcje_f import czytaj_liste,czytaj_slownik

print("to jest program modułowy!")
print("Przydatne skróty:")
print("CTRL + D -> powielenie linii/bloku tekstu")
print("CTRL + /  -> komentowanie/odkomentowanie bloku kodu")
print("___________ lista -> nrfilii _________")
print(nf)

print("___________ słownik -> book _________")
print(bk)

print("___________ lista -> nrfilii -> funkcja czytaj_liste() _________")
czytaj_liste(nf)

print("___________ słownik -> book -> funkcja czytaj_slownik() _________")
czytaj_slownik(bk)
