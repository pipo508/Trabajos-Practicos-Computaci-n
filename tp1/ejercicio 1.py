import random

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
findes = ["sabado", "domingo"]
semana= ["lunes", "martes", "miercoles", "jueves", "viernes","sabado", "domingo"]
dia = random.choice(semana)
print(dia)


def comprobar_dia():
    if dia in dias:
        return True
    elif dia in findes:
        return False


def vacaciones():
    number = random.randint(0, 1)
    if number == 0:
        print("vacaciones")
        return True

    else:
        print("no vacaciones")
        return False


if comprobar_dia() is False and vacaciones() is False:
    print("dormimos")
elif comprobar_dia() is False and vacaciones() is True:
    print("dormimos")
elif comprobar_dia() is True and vacaciones() is True:
    print("dormimos")
elif comprobar_dia() is False and vacaciones() is False:
    print("no dormimos")
else:
    print("no dormimos")
