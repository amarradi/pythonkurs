'''
Schreiben Sie ein Python-Skript, dass...
1. ...überprüft ob eine Zeichenkette ausschließlich aus Buchstaben (klein und groß)
und Zahlen besteht.
'''
import re

var_suchtext = "kannzueinerGruppevonZiffernzusammenstwerdeng09"
var_suchausdruck = "^[a-zA-ZäöüÄÖÜß0-9]+$"
if re.match(var_suchausdruck, var_suchtext):
    print((re.match(var_suchausdruck, var_suchtext)))
else:
    print("enthält Sonderzeichen")
