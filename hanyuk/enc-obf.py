import sys
import webbrowser

def menu():
    print("Menu enkripsi")
    print("1. Enkripsi")
    print("2. Keluar")
    i = input("Pilih: ")
    if i in ['1', '01']:
        webbrowser.open("https://pyob.oxyry.com/")
    elif i in ['2', '02']:
        sys.exit()
    else:
        menu()

menu()
