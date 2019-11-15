"""
IP Adressen aus log ziehen und über geoIP2 abfragen und mit simplekml als kml erzeugen

Quellen: https://pypi.org/project/geoip2/

"""
import simplekml
import geoip2.database
import gzip
import os
import re

var_ip = r"([0-9]{1,3}\.){3}[0-9]{1,3}"
reader = geoip2.database.Reader('GeoLite2-City.mmdb')
kml = simplekml.Kml()
file_content = []
ip_list = []

for var_root, var_dirs, var_files in os.walk('.', topdown=False):
    for var_name in var_files:
        if var_name.endswith('.gz'):
            with gzip.open(os.path.join(var_root, var_name), 'rt') as var_f:
                file_content += var_f.readlines()


for zeile in file_content:
    if 'fatal' in zeile.lower() or 'failed' in zeile.lower():
        try:
            ip_list.append(re.search(var_ip, zeile).group())
        except:
            pass

ip_list = list(set(ip_list))

for ip in ip_list:
    try:
        response = reader.city(ip)
        kml.newpoint(name=ip, coords=[(response.location.longitude, response.location.latitude)])
    except:
        pass

kml.save('attacker.kml')

