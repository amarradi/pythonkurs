'''
Schreiben Sie ein Python-Skript, dass...
6. ...ein Dokument und eine beliebige Anzahl von Suchbegriﬀen übergeben bekommt
und anzeigt ob es Treﬀer gibt.
https://docs.python.org/3/library/argparse.html
'''
import argparse
import re

print("Test")
parser = argparse.ArgumentParser(description='Suchen in einer Datei')
parser.add_argument('file', metavar='F', type=str, help='Name der Datei')
parser.add_argument('searchwords', metavar='S', type=str, nargs='+', help='Suchbegriff(e)')

args = parser.parse_args()
print(args.file)
print(args.searchwords)
matches = []
with open(args.file, 'r', encoding='utf-8') as file:
    filecontent = file.read()
    for searchword in args.searchwords:
        matches += re.finditer(searchword, filecontent)
        matches.append(re.finditer(searchword, filecontent))

for match in matches:
    print(match)
