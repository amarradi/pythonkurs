'''
Schreiben Sie ein Python-Skript, dass...
5. ...alle führenden Nullen einer IP-Adresse entfernt.
'''
import re

var_suchtext = "192.168.002.010"
var_suchausdruck = "[1-9][0-9]{0,2}"
tmp = re.findall(var_suchausdruck, var_suchtext)
print(tmp[0], tmp[1], tmp[2], tmp[3], sep=".")
