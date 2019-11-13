"""
2. Implementiere einen Suchmodus für Dateinamen.
--> Gesucht werden alle Dateien mit 'VeraCrypt' im Namen.
"""
# Lösung 1 #
import os

output = open('output6.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('c:\\', topdown=False):
    for var_name in var_files:
        tmp = var_name.lower()
        if tmp.find('veracrypt') != -1:
            print(os.path.join(var_root, var_name), file=output)
output.close()
# Lösung 2 #
"""
import os
import re
output = open('output6.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('/mnt/ewf1',topdown=False):
    for var_name in var_files:
        tmp = var_name.lower()
        if re.match('[Vv][Ee][Rr][Aa][Cc][Rr][Yy][Pp][Tt]', var_name):
            print(os.path.join(var_root,var_name),file=output)
output.close()
"""