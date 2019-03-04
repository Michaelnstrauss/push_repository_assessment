import os
from orm import ORM
from campus import Campus
from student import Student

DIR = os.path.dirname(__file__)
DBFILENAME = 'school.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath

    NewYork = Campus(city='New York', state='New York')
    NewYork.save()
