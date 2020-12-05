import urllib.request
import os
a = input("podaj strone z plikiem: ")
b = input("podaj nazwe lub patch do pobranego pliku: ")
urllib.request.urlretrieve(a, b)
print("pobieranie zakończone!, plik ma rozmiar: ")
os.system(f"du -sh {b}")