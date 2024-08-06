def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'element listy: {j} -> indeks: {i}')

def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f'słownik -> klucz: {x}, wartośc: {y}')
