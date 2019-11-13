'''
Schreiben Sie ein Python-Skript, dass...
2. ...einen Kleinbuchstaben gefolgt von einem Großbuchstaben ﬁndet.
'''
import re
var_suchtext = "Ba"
var_suchausdruck = "^[a-z][A-Z]+$"
if re.match(var_suchausdruck,var_suchtext):
    print((re.match(var_suchausdruck,var_suchtext)))
else:
    print("Kein Kleinbuchstabe gefolgt von einem Großbuchstaben")
