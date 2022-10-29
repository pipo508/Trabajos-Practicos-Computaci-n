import random

import menu
from items import Items
from constants import *
from menu import select_amount_character, select_race, select_character, remove_character, dice
from enemy_new import *
from login import login, crear_cuenta, comprobar_datos
from random import choice

enemy_names = ["jesu", "fede", "gianca"]
enemy_basic_age = random.randint(1, 3)
enemy_basic_str = random.randint(3, 8)
enemy_basic_agi = random.randint(2, 6)
enemy_basic_con = random.randint(30, 60)
enemy_basic_race = ["orc", "human", "elf"]
enemy_basic_dmg = random.randint(1, 3)
enemy_basic_min_exp = random.randint(100, 150)
enemy_basic_max_exp = random.randint(150, 260)

enemy_control = []

for i in range(10):
    enemy_control.append(Enemy(
        choice(enemy_names),
        enemy_basic_age,
        enemy_basic_str,
        enemy_basic_agi,
        enemy_basic_con,
        choice(enemy_basic_race),
        enemy_basic_dmg,
        enemy_basic_min_exp,
        enemy_basic_max_exp
    ))

    enemy_basic_age += random.randint(1, 10)
    enemy_basic_str += random.randint(1, 5)
    enemy_basic_agi += random.randint(1, 3)
    enemy_basic_con += random.randint(25, 50)
    enemy_basic_dmg += random.randint(1, 3)
    enemy_basic_min_exp += random.randint(100, 200)
    enemy_basic_max_exp += random.randint(100, 200)

items_control = [
    Items("potion", 0, 0, random.randint(50, 100), True),
    Items("sword", random.randint(15, 30), 0, 0, False),
    Items("armor", 0, 0, random.randint(70, 120), False),
    Items("gloves", 0, random.randint(1, 3), 0, False),
    Items("boots", 0, random.randint(6, 10), 0, False),
    Items("shield", random.randint(20, 40), 0, 0, False),
    Items("helm", 0, 0, random.randint(30, 60), False),
    Items("potion_max", 0, 0, random.randint(180, 200), True)
]
character_control = []
character_selected_for_combat = ''
print("\033[;36m" + "")
"""#ingresar o crear cuenta
while True:
    print("1:Crear cuenta: \n2:Ingresar a su cuenta:")
    option = int(input("your option: "))
    if option == 1:
        crear_cuenta()
        break
    elif option == 2:
        while True:
            datos_ingresados = login()
            datos= comprobar_datos(datos_ingresados, crear_cuenta())
            if datos == True:
                break
        break
    else:
        print("su opcion no existe, ingresela nuevamente\n")"""
# cantidad de personajes
amount = select_amount_character()

# seleccion de raza
count = 0
while count != amount:
    character = select_race()
    character_control.append(character)
    count += 1

while True:
    print(MENU_OPTION)
    option = int(input(CHOICE))
    if option == 1:
        character_selected_for_combat = select_character(character_control)
        break
    elif option == 2:
        remove_character(character_control)
    elif option == 3:
        break
    else:
        print(WRONG)

character_turn = True
enemy = enemy_control.pop(0)

if character_selected_for_combat.agi < enemy.agi:
    character_turn = False

while True:
    if len(character_selected_for_combat.inventory) > 0:
        option_selected = menu.check_inventory(character_selected_for_combat.inventory)

        if option_selected >= 0:
            potion_selected = character_selected_for_combat.inventory.pop(option_selected)
            character_selected_for_combat.con += potion_selected.con

    input(FIGHT)
    dice_random = dice()

    if character_turn:
        damage_character = character_selected_for_combat.damage_send(dice_random)
        enemy.damage_received(damage_character)
        print(DAMAGE_CAUSED, f"{character_selected_for_combat.name} -----> {damage_character}", HEALTH_POINTS)
        print(CURRENT_HEALTH, f"{enemy.name}:", round(enemy.con, 1), HEALTH_POINTS)
        character_turn = False

        if enemy.dead:
            print(f"{enemy.name}", DEAD)
            exp_earn = enemy.give_exp()
            character_selected_for_combat.exp = exp_earn / (len(character_control) + 1)
            character_selected_for_combat.check_to_next_level()

            if random.randint(1, 100) <= 50:
                item_dropped = items_control.pop(random.randint(0, len(items_control) - 1))
                if item_dropped.cons:
                    character_selected_for_combat.inventory.append(item_dropped)
                    print("se añadio la pocion al inventario")
                else:
                    character_selected_for_combat.agi += item_dropped.agi
                    character_selected_for_combat.con += item_dropped.con
                    character_selected_for_combat.strength += item_dropped.str
                    print(f"has conseguido el item{item_dropped.name}")

            if len(character_control) >= 1:
                exp_earn /= len(character_control) + 1
                for i in character_control:
                    i.exp += exp_earn
                    i.check_to_next_level()
            if len(enemy_control) >= 1:
                enemy = enemy_control.pop(0)
            else:
                break

    else:
        damage_enemy = enemy.damage_send(dice_random)
        character_selected_for_combat.damage_received(damage_enemy)
        if character_selected_for_combat.dead:
            print(f"{character_selected_for_combat.name}", DEAD)
            if len(character_control) > 0:
                character_selected_for_combat = select_character(character_control)
            else:
                break

        print(DAMAGE_CAUSED, f"{enemy.name} -----> {damage_enemy}", HEALTH_POINTS)
        print(CURRENT_HEALTH, f"{character_selected_for_combat.name}:", round(character_selected_for_combat.con, 1),
              HEALTH_POINTS)
        character_turn = True
