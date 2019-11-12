print("Strn+c beendet das Programm")
try:
    while True:
        try:
            zahl1 = int(input("1. Zahl: "))
            zahl2 = int(input("2. Zahl: "))
            print(zahl1, "+", zahl2, "=", zahl1 + zahl2)
        except ValueError:
            print("Keine Zahl")
except KeyboardInterrupt:
    pass