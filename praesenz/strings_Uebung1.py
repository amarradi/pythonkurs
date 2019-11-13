# Uebungen zu Strings


'''
Uebung 1

Nutzen Sie string.split() und .format() und setzen Sie den String korrekt zusammen.
'''

string1 = 'Teile eines Computer die Hardware nennt man die man treten kann'
# Hardware nennt man die Teile eines Computer die man treten kann
# ['Teile', 'eines', 'Computer', 'die', 'Hardware', 'nennt', 'man', 'die', 'man', 'treten', 'kann']
print(string1)
string2 = string1.split()
print(string2)
var_ausgabe = "{} {} {} {} {} {} {} {} {} {} {}".format(string2[4], string2[5], string2[6], string2[3], string2[0],
                                                        string2[1], string2[2], string2[3], string2[8], string2[9],
                                                        string2[10])
print(var_ausgabe)
