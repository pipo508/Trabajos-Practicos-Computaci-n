import random

from torre_control import Torre_control
import time
from despegar import Despegar
from aterrizar import Aterrizar

despegar = Despegar()
aterrizar = Aterrizar()
torre = Torre_control()
random1 = random.randint(1, 5)
random2 = random.randint(1, 5)
aterrizar.push_aviones_volando(random1)
despegar.push_aviones_tierra(random2)
while True:
    print("\n1:Estado de los aviones\n2:Activar torre de control")
    opcion = int(input("Su opcion: "))
    if opcion == 1:
        print(torre.__str__())
    elif opcion == 2:
        contador = 0
        numero = random1 + random2
        while True:
            time.sleep(2)
            torre.reconocimiento()
            contador += 1
            if contador == (random2+random1+1):
                break
        print("\n No hay mas aviones")
        break
