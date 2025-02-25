import os

path = "C:/Users/uzzer/Desktop/ПП2/pp2/L6/file3"

if os.path.exists(path):
    os.remove(path)
else:
    print("The file does not exist")