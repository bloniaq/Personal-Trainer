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
        db_path = './profiles/' + self.login + '.db'
        self.con = sqlite3.connect(db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

        Person.__init__(self)


    def create_profile(self, name: str, sex: str, height: int, date_of_birth):
        self.cur.execute("DROP TABLE IF EXISTS person;")

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS person (
                login text,
                name text,
                sex text,
                height INTEGER,
                dateofbirth text
            );""")

        person_data = (self.login, name, sex, height, date_of_birth)

        insert_sql = """INSERT INTO person 
            (login, name, sex, height, dateofbirth)
            VALUES (?, ?, ?, ?, ?);"""

        self.cur.execute(insert_sql, person_data)
