eingabe = '355654081307790'
def validate_luhn():
    liste = list(eingabe)
    liste.reverse()
    summe = 0
    for index, zeichen in enumerate(liste):
        ziffer = int(zeichen)
        if index % 2 == 0:
            summe = summe+ziffer
        else:
            ziffer = ziffer * 2
            if (ziffer > 9):
                ziffer = ziffer - 9
            summe = summe + ziffer
    if summe % 10 == 0 and len(eingabe) == 15:
        print("Es handelt sich bei der IMEI um eine gültige IMEI")
    else:
        print("Es handelt sich bei der IMEI um NICHT eine gültige IMEI")
validate_luhn()