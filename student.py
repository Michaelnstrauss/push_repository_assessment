import sqlite3
from orm import ORM
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'school.db'
DBPATH = os.path.join(DIR, DBFILENAME)
TXTFILENAME = 'school_info.txt'
TXTPATH = os.path.join(DIR, TXTFILENAME)

class Student(ORM):
    tablename = 'students'
    fields = ['first_name','last_name', 'campuses_pk', 'gpa']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.campuses_pk = kwargs.get('campuses_pk')