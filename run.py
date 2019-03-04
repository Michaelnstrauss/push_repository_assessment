#! /usr/bin/env python3
from campus import Campus
from student import Student
import os
from orm import ORM

DIR = os.path.dirname(__file__)
DBNAME = 'school.db'
DBPATH = os.path.join(DIR, 'data', DBNAME)

ORM.dbpath = DBPATH
bk = Campus(city="city")
bk.load_text()
# bkm = Word(word_count='word count')
# bkm.makeword(word)