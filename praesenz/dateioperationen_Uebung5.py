"""
4. Implementiere einen Suchmodus für Zeitstempel (bspw. a-time)
   Tipp:
   --> from datetime import date
   --> date.<Vorschläge>
"""
import hashlib
import os

var_sha256 = hashlib.sha256()
var_eingabe = "4070df65bf9ba887be7d2e66508b2486cebeface0540a3730f76852ce06f3e78"

output = open('dateioperationen_Uebung5.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('/mnt/ewf1', topdown=False):
    for var_name in var_files:
        tmp = var_sha256.update(str(os.stat(os.path.join(var_root, var_name))))
        if str(var_sha256.hexdigest()) == var_eingabe:
            print(os.path.join(var_root, var_name), file=output)
output.close()
