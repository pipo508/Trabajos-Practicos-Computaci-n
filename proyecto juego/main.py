from menu import select_amount_character, select_race, select_character, remove_character, dice
from enemy_new import Enemy

enemy_control = [
    Enemy("batman", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("super hijitus", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("robin", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("penguin", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("joker", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("flash", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("wonder woman", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("catwoman", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("harley quinn", 16, 7, 3, 50, "orc", 2, 100, 200),
    Enemy("constantine", 16, 7, 3, 50, "orc", 2, 100, 400)
]
character_control = []
character_selected_for_combat = ''
print("\033[;36m" + "")
# cantidad de personajes
amount = select_amount_character()

# seleccion de raza
count = 0
while count != amount:
    character = select_race()
    character_control.append(character)
    count += 1

while True:
    print("Choose the option you want to perform:\n 1: Choose character\n 2: Remove character:\n 3: Exit")
    option = int(input("Your option"))
    if option == 1:
        character_selected_for_combat = select_character(character_control)
        break
    elif option == 2:
        remove_character(character_control)
    elif option == 3:
        break
    else:
        print("Your option is incorrect")
character_turn = True
enemy = enemy_control.pop(0)
while True:
    input("presiona una tecla para pelear")
    dice_random = dice()
    if character_turn:
        damage_character = character_selected_for_combat.damage_send(dice_random)
        enemy.damage_recived(damage_character)
        print(f"Daño causado por:{character_selected_for_combat.name}> {damage_character}")
        print(f"Vida actual de: {enemy.name}", enemy.con)
        character_turn = False

        if enemy.dead:
            print(f"{enemy.name} MURIO.")
            exp_earn = enemy.give_exp()
            character_selected_for_combat.exp = exp_earn / (len(character_control) + 1)
            character_selected_for_combat.check_to_next_level()
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
        character_selected_for_combat.damage_recived(damage_enemy)
        if character_selected_for_combat.dead:
            print(f"{character_selected_for_combat.name} MURIO.")
            if len(character_control) > 0:
                character_selected_for_combat = select_character(character_control)
            else:
                break

        print(f"Daño causado por:{enemy.name}> {damage_enemy}")
        print(f"Vida actual de: {character_selected_for_combat.name}", character_selected_for_combat.con)
        character_turn = True