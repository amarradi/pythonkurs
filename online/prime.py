var_zahl = 2
while var_zahl < 100:
    var_teiler = 2
    while var_teiler < var_zahl:
        if var_zahl % var_teiler == 0:
            break
        var_teiler += 1
    else:
        print(var_zahl, "ist Primzahl")
    var_zahl += 1
