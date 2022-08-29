from aterrizar import Aterrizar
from despegar import Despegar
import time

despegar = Despegar()
aterrizar = Aterrizar()


class Torre_control:
    def __str__(self):
        return f"Estos aviones se encuentran en vuelo : {aterrizar.estado()}\nEstos aviones se encuentran en tierra : {despegar.estado()}"

    def reconocimiento(self):
        contador = 0
        while contador <= 3:
            if despegar.accion() is True and aterrizar.accion() is False:
                print("\n")
                despegar.quien_despega()
                time.sleep(1)
                print("El avion esta despegando ... ")
                time.sleep(2)
                print("El avion", despegar.despegar_pop(), "despegó correctamente")
                break
            elif despegar.accion() is False and aterrizar.accion() is True:
                print("\n")
                aterrizar.quien_Aterriza()
                time.sleep(1)
                print("El avion esta aterrizando ... ")
                time.sleep(2)
                print("El avion", aterrizar.aterrizar_pop(), "aterrizo correctamente")
                break
            elif despegar.accion() is True and aterrizar.accion() is True:
                print("\n")
                despegar.quien_despega()
                aterrizar.quien_Aterriza()
                print("dos aviones quieren utilizar la pista asique le damos prioridad al que tiene que aterrizar")
                time.sleep(1)
                print("El avion esta aterrizando ... ")
                time.sleep(2)
                print("El avion", aterrizar.aterrizar_pop(), "aterrizo correctamente")
                break
            else:
                if len(aterrizar.estado()) == 0 and len(despegar.estado()) == 0:
                    break
                else:
                    pass
