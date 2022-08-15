from os import path

file_name = input("file name: ")
try:
    file = open(file_name)
    print(file.read())
    ler = file.read()
    print(ler)
except FileNotFoundError:
    print("file not found!")