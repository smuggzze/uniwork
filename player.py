from random import randint
player = {"name": "Sheldor", "health": 79, "xp": 0, "mana": 100, "alive": True, "inventory": [ ]}


def print_player(cheese):
    for attributes in cheese:
        if attributes == "name":
            print("name is", cheese[attributes])
        if attributes == "health":
            print("health is", cheese[attributes])
        if attributes == "experience":
            print("experience is", cheese[attributes])
        if attributes == "mana":
            print("mana is", cheese[attributes])
        if attributes == "inventory":
            print("inventory is", cheese[attributes])


def compute_experience(damage):
    exp = randint(0, damage*2)
    return exp


def take_damage(player, dmg):
    player["health"] -= dmg
    player["xp"] += compute_experience(dmg)
    if player["health"] <= 0:
        player["alive"] = False
    return player

while player["health"] >= 0:
    take_damage(player, 4)
    print_player(player)

