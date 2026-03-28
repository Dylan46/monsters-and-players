import random
from commands import register
from weapons import weapons
from player import player

monsters = {
    "goblin": 2,
    "troll": 4,
    "dragon": 6
}

def fight_monster():

    if player.weapon is None:
        print("You have no weapon! The monster defeats you.")
        return

    monster = random.choice(list(monsters.keys()))

    monster_strength = monsters[monster]
    weapon_strength = weapons[player.weapon]

    print(f"A wild {monster} appears!")
    print(f"You attack with your {player.weapon}")

    if weapon_strength >= monster_strength:
        print("You defeated the monster!")
    else:
        print("The monster was too strong... you lost!")

register("fight", fight_monster)