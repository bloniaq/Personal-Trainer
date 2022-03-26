import trainer.models.profile as profile
from trainer.models.dataseries import CATALOG as catalog

import datetime as dt
import sqlite3


class TestProfile:

    def test_init(self):
        prof = profile.Profile('stefan')
        assert prof is not None
        assert profile.Person().__dict__.items() <= prof.__dict__.items()
        assert prof.login is 'stefan'

    def test_create_profile(self):
        prof = profile.Profile('stefan')
        prof.create_profile('Stefan', 'male', 175, '1973-04-20')
        assert isinstance(prof.con, sqlite3.Connection)
        cur = prof.con.cursor()
        cur.execute("SELECT * FROM person")
        person = cur.fetchall()
        print(person)
        assert person[0]['login'] == 'stefan'
        assert person[0]['name'] == 'Stefan'
        assert person[0]['sex'] == 'male'
        assert person[0]['height'] == 175
        assert person[0]['dateofbirth'] == '1973-04-20'


class TestPerson:

    def test_init(self):
        person = profile.Person()
        assert person is not None
        assert person.name is ''
        assert person.birth_date == dt.datetime(1970, 1, 1, 0, 0)
        assert person.sex is 'unknown'
        assert person.height == 0

    def test_set_name(self):
        person = profile.Person()
        assert person.name is ''
        test_name = "Ziutek"
        person.set_name(test_name)
        assert person.name == test_name

    def test_set_height(self):
        person = profile.Person()
        test_height = 220
        person.set_height(test_height)
        assert person.height == test_height

    def test_set_sex(self):
        person = profile.Person()
        person.set_sex('male')
        assert person.sex == 'male'
        person.set_sex('female')
        assert person.sex == 'female'

    def test_set_brithdate(self):
        person = profile.Person()
        test_bdate = dt.datetime(1990, 8, 28)
        person.set_birthdate(test_bdate)
        assert person.birth_date == test_bdate
        assert person.birth_date == dt.datetime(1990, 8, 28, 0, 0)
