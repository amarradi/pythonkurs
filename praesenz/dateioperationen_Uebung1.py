'''
1. Schreibe ein Programm, dass alle Dateien im Verzeichnis /mnt/ewf1/ (Mountpoint von Win7_Python.E01) durchläuft.

--> Ausgegeben werden soll (Zeile für Zeile) der komplette
    Pfade jeder gefundenen Datei unterhalb des Mountpoints.

'''

import os

output = open('dateioperationen_Uebung1_output.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('c:\\', topdown=False):
    for var_name in var_files:
        print(os.path.join(var_root, var_name), file=output)
