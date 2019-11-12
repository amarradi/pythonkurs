# t = (1,)
# l = [1,2,3,4]
# d = {'eins':1, 'zwei':2}
#
# s = "Hallo Welt!"
# for var_buchstabe in s:
#     print(var_buchstabe)
#
# var_summe = 0
# for var_zahl in l:
#     var_summe = var_summe + var_zahl
# print(var_summe)
#
# for var_index, var_element in enumerate(s):
#     print("index", var_index, "element", var_element)
var_dozenten = (('Markus','Klie'),('Patrick', 'Eisoldt'))
#print(var_dozenten[1][0])
for vorname, nachname in var_dozenten:
    print("Vorname", vorname)
    print("Nachname", nachname)