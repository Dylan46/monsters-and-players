import random
from commands import register
from player import player

weapons = {
    "stick": 1,
    "sword": 3,
    "magic sword": 5
}

def find_weapon():
    weapon = random.choice(list(weapons.keys()))
    player.weapon = weapon
    print(f"You found a {weapon}!")

register("search", find_weapon)