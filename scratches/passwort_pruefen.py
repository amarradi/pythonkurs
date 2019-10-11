#Passwort Prüfen
'''
Überprüfen Sie die Nutzereingabe eines Passwortes auf Gültigkeit. GebenSie eine Erfolgs- oder Misserfolgsmeldung aus. Das Passwort soll folgendeBedinungen erfüllen:
1. PW hat eine Länge von 6 Zeichen
2. PW beginnt mit einem Großbuchstaben
3. PW das 3. und 6. Zeichen ist eine Zahl und
das Passwort darf nur Zahlen und Buchstaben enthalten
'''

passwort = input("Bitte geben Sie ein Passwort ein:")


if passwort.isalnum() != True:
    print("Das Passwort darf nur aus Buchstaben und Ziffern bestehen")
elif len(passwort) != int(6):
    print("Ihr Passwort ist zu kurz oder zu lang")
elif passwort[0].isupper() != True:
    print("Das erste Zeichen muss GROß geschrieben werden")
elif passwort[2].isdecimal() != True or passwort[5].isdecimal() != True:
    print("Das 3. und 6. Zeichen muss ein Buchstabe oder eine Zahl sein")
