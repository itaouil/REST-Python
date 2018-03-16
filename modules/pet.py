import pymysql.cursors

class Pet:

    def __init__(self, name, species, gender, birthday):
        self.name = name
        self.species = species
        self.gender = gender
        self.birthday = birthday
