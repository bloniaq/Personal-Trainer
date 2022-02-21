import datetime as dt


class Person:

    def __init__(self):
        self.name = ''
        self.birth_date = dt.datetime(1970, 1, 1, 0, 0)
        self.sex = None
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

    pass
