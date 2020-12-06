import urllib.request
import os.path
from threading import Thread
import time
import os
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
content = int(site.headers['Content-Length'])
try:
    Thread(target=progressbar).start()
    urllib.request.urlretrieve(url, local_filename)
except:
    usun = input("chcesz usunąć plik? (y/n): ")
    if usun == 'y':
        os.system(f'{local_filename}')
    else:
        pass
#print(site.info())
size = os.path.getsize(local_filename)
print("pobieranie zakończone!, plik ma rozmiar: ", size / 1048576 , "mb")