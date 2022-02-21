import trainer.models.profile as profile

import datetime as dt


class TestProfile:

    def test_init(self):
        prof = profile.Profile()
        assert prof is not None
        assert profile.Person().__dict__.items() <= prof.__dict__.items()
        assert prof.name is ''
        assert prof.birth_date == dt.datetime(1970, 1, 1, 0, 0)


class TestPerson:

    def test_init(self):
        person = profile.Person()
        assert person is not None
        assert person.name is ''
        assert person.birth_date == dt.datetime(1970, 1, 1, 0, 0)
        assert person.sex is None
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
