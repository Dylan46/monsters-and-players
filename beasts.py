import random
from commands import register
from weapons import weapons
from player import player


class Beast:
    def __init__(self, name, strength=5):
        self.name = name
        self.strength = strength    # Default strength for all  
        self.health = 100           #   Default initial health for all beasts
        self.statusAlive = True     #   Default initial status for all beasts

    def reduceHealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.statusAlive = False
        else:
            self.statusAlive = True


