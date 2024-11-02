import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.home = home
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, manege):
        pass

    def chill(self):
        pass

    def clean_house(self):
        pass

    def to_repair(self):
        pass

    def day_index(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption":6},
    "Lada":{"fuel":50, "strength": 40, "consumption":10},
    "Volvo":{"fuel":70, "strength":150, "consumption":8},
    "Ferrari":{"fuel":80, "strength":120, "consumption":14}
}

class Auto:
    def __init__(self):
        pass