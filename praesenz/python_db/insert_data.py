"""
Quelle: https://www.sqlitetutorial.net/sqlite-python/insert/
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
    create a database connection to the SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_film(conn, film):
    """
    Create a new film
    :param conn:
    :param film:
    :return:
    """
    sql = ''' INSERT INTO films(name,jahr,sprache)
                VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, film)
    conn.commit()
    return cur.lastrowid


def create_meta(conn, meta):
    """
    Create a new metadata
    :param conn:
    :param meta:
    :return:
    """
    sql = ''' INSERT INTO metas(film_id,qualitaet,dauer_min)
                VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, meta)
    conn.commit()
    return cur.lastrowid


def main():
    database = "filmliste_py.db"
    conn = create_connection(database)
    with conn:
        film = ('Per Anhalter durch die Galaxis', '2005', 'deutsch')
        film_id = create_film(conn, film)
        meta_1 = (film_id, 'sehr gut', '110')
        create_meta(conn, meta_1)


if __name__ == '__main__':
    main()
