"""
Schreiben Sie ein Python-Skript, dass...
8. ...ein Datum in dem Format yyyy-mm-dd oder yy-m-d in das Format dd.mm.yyyy konvertiert.
"""
import re

var_suchtext = "2019-11-13"
var_suchausdruck = "([0-9]{2,4})-([0-9]{1,2})-([0-9]{1,2})"
print(re.findall(var_suchausdruck, var_suchtext))
ergebnis = re.findall(var_suchausdruck, var_suchtext)
print(ergebnis[0][2], ergebnis[0][1], ergebnis[0][0], sep='.')
