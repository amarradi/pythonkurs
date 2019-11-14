"""
Aufgabe SQLite:
Führen Sie jeden Schritt zunächst mit dem DB Browser und dann noch einmal in Python aus!
- Erstellen Sie eine SQLite Datenbank mit dem Namen 'filmliste_browser.db' (mit dem DB Browser) und 'filmliste_py.db' (mit Python).
- die Datenbank soll die Tabelle 'filme' mit den Spalten
  id(integer),name(text),jahr(integer),sprache(text) enthalten.
- die Datenbank soll eine zweite Tabelle 'meta' mit den
  film_id(integer),qualitaet(text),dauer_min(integer) enthalten.
- die Tabellen sind untereinander mit den Spalten id und film_id
  referenziert.
- Füllen Sie die DB mit Beispielswerten
- Erstellen Sie einen CSV Report nach dem Muster: film
  (name),qualität,dauer

Nutzen Sie zur Umsetzung die drei Funktionen:

create_db(): zum Erstellen und Befüllen der Datenbank
abfrage_db(): zur Durchführung einer Abfrage
export_csv(): zum Export in die Datei filmliste.csv
"""
import sqlite3

curs = sqlite3.connect('filmliste_py.db')
create_table_filme = """CREATE TABLE IF NOT EXISTS filme (
id integer PRIMARY KEY AUTOINCREMENT,
name text,
jahr integer,
sprache text );"""

create_table_meta = """CREATE TABLE IF NOT EXISTS meta (
id integer PRIMARY KEY AUTOINCREMENT,
film_id integer,
qualitaet text,
dauer_min integer);"""

insert_into_filme = """INSERT INTO 'filme' ('name','jahr','sprache') VALUES ('Mr. Robot Staffel 1', '2015', 'englisch');"""
insert_into_meta = """INSERT INTO 'meta' ('film_id', 'qualitaet', 'dauer_min') VALUES ('1', 'sehr gut', '400');"""
curs.execute(create_table_filme)
curs.execute(create_table_meta)
curs.execute(insert_into_filme)
curs.execute(insert_into_meta)
curs.commit()
