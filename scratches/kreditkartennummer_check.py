eingabe = '5500000000000003'
liste = list(eingabe)
liste.reverse()
summe = 0
for index, zeichen in enumerate(liste):
    ziffer = int(zeichen)
    if index % 2 == 0:
        summe = summe + ziffer
    else:
        ziffer = ziffer * 2
        if ziffer > 9:
            ziffer = ziffer - 9
        summe = summe + ziffer
if summe % 10 == 0 and len(eingabe) == 16:
    print("Es handelt sich bei der Kreditkartennummer um eine gültige Kreditkartennummer")
else:
    print("Es handelt sich bei der Kreditkartennummer um NICHT eine gültige Kreditkartennummer")