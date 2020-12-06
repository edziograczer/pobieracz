import urllib.request
import os
def pobieracz(edzio, edzio2):
    urllib.request.urlretrieve(a, b)
    print("pobieranie zakończone!, plik ma rozmiar: ")
    os.system(f"du -sh {b}")
a = input("podaj strone z plikiem: ")
b = input("podaj nazwe lub patch do pobranego pliku: ")
pobieracz(a, b)
#tes