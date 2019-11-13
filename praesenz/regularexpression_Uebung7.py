"""
Schreiben Sie ein Python-Skript, dass...
7. ...die exakte Position eines Suchworts in einer Zeichenkette ausgibt.
"""
import re

var_gefunden = False
var_suchtext = "Das ist ein Text in dem ein bestimmtes Wort zu suchen ist und dessen Position auszugeben ist."
var_suchausdruck = "is"
print(re.finditer(var_suchausdruck, var_suchtext))
for i in re.finditer(var_suchausdruck, var_suchtext):
    var_gefunden = True
    s = i.start()
    e = i.end()
    print(s, e, sep=':')

if (var_gefunden):
    print("gefunden")
else:
    print("nicht gefunden")
