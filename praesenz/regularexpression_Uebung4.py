"""
Schreiben Sie ein Python-Skript, dass...
4. ...alle Wörter ﬁndet die ein „y“ enthalten.
"""
import re

var_suchtext = "Xylophon ypsilon funny y"
var_suchausdruck = "[a-zA-Z]*[yY][a-zA-Z]*"

print(re.findall(var_suchausdruck, var_suchtext))
