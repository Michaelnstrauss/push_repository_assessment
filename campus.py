import sqlite3
from orm import ORM
from student import Student
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'school.db'
DBPATH = os.path.join(DIR, DBFILENAME)
TXTFILENAME = 'school_info.txt'
TXTPATH = os.path.join(DIR, TXTFILENAME)

class Campus(ORM):
    tablename = 'campuses'
    fields = ['city', 'state']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')

    @classmethod
    def from_title(cls,city):
        """ return campus object for a given city in the database """
        return cls.select_one_where('WHERE city = ?', (city,))


    def load_text(self, dbpath='school.db'):
        """ load a text file's content into the book's text content """
        with open(TXTPATH,'r') as txt_file:
            lines = txt_file.readlines()
            text_word = ''
            for line in lines:
                splitted_lines = line.split()
                for word in splitted_lines:
                    char = '!$/\'%*+=?\'\-.,*#[]()1234567890;:'
                    word = word.strip(char)
                    text_word += " " + word
            # self.title = input('Input new title: ')
            # self.author = input('Author name: ')
            self.city= text_word
            self.save()