"""
3. Implementiere einen Suchmodus für Dateigrößen.
-> Gesucht wird eine Datei mit 3010349 Byte
"""
import os

output = open('output7.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('c:\\', topdown=False):
    for var_name in var_files:
        if os.stat(os.path.join(var_root, var_name)).st_size == 3010349:
            print(os.path.join(var_root, var_name), file=output)
output.close()