'''
Schreiben Sie ein Python-Skript, dass...
9. ...alle URLs aus einer Zeichenkette herausﬁltert.
'''

import re

var_suchtext = "www.iana.org"
var_suchausdruck = r"[a-zA-Z0-9.:/]+\.[A-Za-z.]{2,}[A-Za-z.:/?=&+_-]*"
print(re.search(var_suchausdruck, var_suchtext))

