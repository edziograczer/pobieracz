import urllib.request
import os.path
import multiprocessing
import time
import os
try:
    system = os.name
    def progressbar():
        while True:
            time.sleep(1.5)
            size2 = os.path.getsize(local_filename)
            if system == 'posix' or 'linux' or 'unix':
                os.system('clear')
            elif system == 'nt' or 'windows':
                os.system('cls')
            else:
                os.system('cls')
            print(f"pobrałeś: {size2 / 1048576} a zostało ci: {content / 1048576}")
            if size2 == content:
                break
    url = input("podaj strone z plikiem: ")
    x = url.split("/")
    local_filename = input("nazwa pliku (domyślna enter): ")
    if local_filename == "":
        local_filename = x[-1]
    site = urllib.request.urlopen(url)
    if site.headers['Content-Length']:
        content = int(site.headers['Content-Length'])
        watek = multiprocessing.Process(target=progressbar)
        watek.start()
        urllib.request.urlretrieve(url, local_filename)
    if not site.headers['Content-Length']:
        urllib.request.urlretrieve(url, local_filename)
        print("pobierasz pewnie text lub html i nie ma rozmiaru pliku :(")
    #print(site.info())
    size = os.path.getsize(local_filename)
    print("pobieranie zakończone!, plik ma rozmiar: ", size / 1048576 , "mb")
except KeyboardInterrupt:
    watek.terminate()
    if system == 'posix' or 'linux' or 'unix':
        os.system('clear')
    elif system == 'nt' or 'windows':
        os.system('cls')
    else:
        os.system('clear')
    zapytajnik = input("chcesz usunąć plik? (y/n): ")
    if zapytajnik == 'y':
        os.remove(local_filename)
        exit()
    else:
        print("bye!")
        exit()