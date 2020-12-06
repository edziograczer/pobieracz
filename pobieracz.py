import urllib.request
import os
def pobieracz(edzio, edzio2):
    urllib.request.urlretrieve(a, b)
    print("pobieranie zakończone!, plik ma rozmiar: ")
    os.system(f"du -sh {b}")
a = input("podaj strone z plikiem: ")
x = a.split("/")
b = input("nazwa pliku (domyślna enter): ")
if b == "":
    b = x [-1]
    print(b)
pobieracz(a, b)