vokale =['a','e','i','o','u']

eingabe = input("Bitte geben Sie ein Wort ein, dass nach Vokalen durchsucht werden soll: ")
for buchstabe in eingabe:
    if buchstabe in vokale:
        print("Ihr Wort enthält einen Vokal.")
        break