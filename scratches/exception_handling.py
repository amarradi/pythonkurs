wert = input("Eingabe bitte: ")
try:
    wert = int(wert)
except ValueError:
    print(str(ValueError))
