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

Quelle: https://www.sqlitetutorial.net/sqlite-python/create-tables/
"""
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "filmliste_py.db"

    sql_create_films_table = """ CREATE TABLE IF NOT EXISTS films (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    name text,
                                    jahr integer,
                                    sprache text
                                ); """
    sql_create_metas_table = """ CREATE TABLE IF NOT EXISTS metas (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    film_id integer,
                                    qualitaet text,
                                    dauer_min integer,
                                    FOREIGN KEY (film_id) REFERENCES films (id)
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_films_table)

        create_table(conn, sql_create_metas_table)
    else:
        print("Fehler, Datenbank kann nicht angelegt werden.")


if __name__ == '__main__':
    main()
