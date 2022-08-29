from menu import select_amount_character, select_race, select_character, remove_character, dice
from enemy_new import Enemy
from login import login, crear_cuenta, comprobar_datos

enemy = Enemy("batman", 16, 7, 3, 50, "orc", 2)
character_control = []
character_selected_for_combat = ''
print("\033[;36m" + "")
#ingresar o crear cuenta
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
        print("su opcion no existe, ingresela nuevamente\n")
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
while True:
    input("presiona una tecla para pelear")
    dice_random = dice()
    if character_turn:
        damage_character = character_selected_for_combat.damage_send(dice_random)
        enemy.damage_recived(damage_character)
        if enemy.dead:
            print(f"{enemy.name} MURIO.")
            break
        print(f"Daño causado por:{character_selected_for_combat.name}> {damage_character}")
        print(f"Vida actual de: {enemy.name}", enemy.con)
        character_turn = False

    else:
        damage_enemy = enemy.damage_send(dice_random)
        character_selected_for_combat.damage_recived(damage_enemy)
        if character_selected_for_combat.dead:
            print(f"{character_selected_for_combat.name} MURIO.")
            break

        character_selected_for_combat= character_control[0]
        print(f"Daño causado por:{enemy.name}> {damage_enemy}")
        print(f"Vida actual de: {character_selected_for_combat.name}", character_selected_for_combat.con)
        character_turn = True
