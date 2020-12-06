import urllib
import os.path
a = input("podaj strone z plikiem: ")
x = a.split("/")
b = input("nazwa pliku (domyślna enter): ")
if b == "":
    b = x [-1]
urllib.request.urlretrieve(a, b)
size = os.path.getsize(f'{b}')
print("pobieranie zakończone!, plik ma rozmiar: ", size , "bajtów")