"""
Schreiben Sie ein Python-Skript, dass...
5. ...alle führenden Nullen einer IP-Adresse entfernt.
"""
import re

#
# Lösung 1
#
var_suchtext = "192.168.002.010"
var_suchausdruck = r"[1-9][0-9]{0,2}"
tmp = re.findall(var_suchausdruck, var_suchtext)
print(tmp[0], tmp[1], tmp[2], tmp[3], sep=".")
#
# Lösung 2
#
# var_suchtext = "192.168.002.010"
# var_suchausdruck = r"([1-9][0-9]{0,2})\.0*([1-9][0-9]{0,2})\.0*([1-9][0-9]{0,2})\.0*([1-9][0-9]{0,2})"
# print(re.sub(var_suchausdruck,r'\1.\2.\3.\4',var_suchtext ))
