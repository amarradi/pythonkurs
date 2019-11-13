"""
4. Implementiere einen Suchmodus für Zeitstempel (bspw. a-time)
   Tipp:
   --> from datetime import date
   --> date.<Vorschläge>
"""
import os
from datetime import date

var_eingabe = input("Bitte geben Sie ein Datum in der Form dd.mm.jjjj ein: ")

output = open('dateioperationen_Uebung4.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('c:\\', topdown=False):
    for var_name in var_files:
        if str(date.fromtimestamp(os.stat(os.path.join(var_root, var_name)).st_atime).strftime(
                "%d.%m.%Y")) == var_eingabe:
            print(os.path.join(var_root, var_name), file=output)
output.close()
