"""
5. Implementieren Sie einen Suchmodus für SHA256-Hashwerte
-> Gesucht wird eine Datei mit dem Hashwert c6a91cba00bf87cdb064c49adaac82255cbec6fdd48fd21f9b3b96abf019916b
"""
import hashlib
import os

var_BLOCKSIZE = 65536

var_searched_hash = "4070df65bf9ba887be7d2e66508b2486cebeface0540a3730f76852ce06f3e78"

output = open('dateioperationen_Uebung5.txt', 'w', encoding='utf-8')
for var_root, var_dirs, var_files in os.walk('c:\\', topdown=False):
    for var_name in var_files:
        with open(os.path.join(var_root, var_name), 'rb') as var_file:
            var_fbuf = var_file.read(var_BLOCKSIZE)
            var_sha256 = hashlib.sha256()
            while len(var_fbuf) > 0:
                var_sha256.update(var_fbuf)
                var_fbuf = var_file.read(var_BLOCKSIZE)
            tmp = os.path.join(var_root, var_name), var_sha256.hexdigest()
            if str(tmp[1]) == var_searched_hash:
                print(os.path.join(var_root, var_name), var_sha256.hexdigest(), sep=':', file=output)
