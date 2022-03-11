import datetime as dt
import sqlite3
from trainer.models.dataseries import CATALOG as catalog


class Person:

    def __init__(self):
        self.name = ''
        self.birth_date = dt.datetime(1970, 1, 1, 0, 0)
        self.sex = 'unknown'
        self.height = 0

    def set_name(self, new_name):
        self.name = new_name

    def set_height(self, new_height):
        self.height = new_height

    def set_sex(self, new_sex):
        self.sex = new_sex

    def set_birthdate(self, new_date):
        self.birth_date = new_date


class Profile(Person):

    def __init__(self, login):

        self.login = login
        self.db_path = './profiles/' + self.login + '.db'

        Person.__init__(self)


    def create_profile(self, name: str, sex: str, height: int, db_path):
        self.name = name
        self.sex = sex
        self.height = height
        print(db_path)
        self.con = sqlite3.connect(db_path)
