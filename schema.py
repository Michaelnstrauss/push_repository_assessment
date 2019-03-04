import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'school.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = 'DROP TABLE IF EXISTS {tablename};'

        cur.execute(DROPSQL.format(tablename='campuses'))

        SQL = '''CREATE TABLE campuses(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                city VARCHAR(128) NOT NULL,
                state VARCHAR(128),
                UNIQUE(city)
            );'''

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename='students'))

        SQL = '''CREATE TABLE students(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            campuses_pk INT,
            first_name VARCHAR(128) NOT NULL,
            last_name VARCHAR(128),
            gpa FLOAT,
            FOREIGN KEY(campuses_pk) REFERENCES campuses(pk),
            UNIQUE(campuses_pk, first_name)
            );'''

        cur.execute(SQL)

if __name__=='__main__':
    schema()