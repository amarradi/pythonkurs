import sqlite3

curs = sqlite3.connect('buecher.db')

var_eingabe = input("Eingabe bitte: ")
for row in curs.execute('SELECT * FROM buecher WHERE id = ?',
                        (var_eingabe,)):
    print(row)
curs.close()
