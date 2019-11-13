"""
Schreiben Sie ein Python-Skript, dass...
3. ...überprüft ob eine Zeichenkette mit einem Wort beginnt.
"""
import re

var_suchtext = "Ba fgdfgdff erte "
var_suchausdruck = "^[a-zA-Zäöüß]{2,}\s"
if re.match(var_suchausdruck, var_suchtext):
    print((re.match(var_suchausdruck, var_suchtext)))
else:
    print("Kein Wort am Zeilenanfang")
