import random


class Despegar:
    aviones_tierra = []

    def push_aviones_tierra(self, cantidad):
        contador = 0
        while contador < cantidad:
            numero = random.randint(100, 999)
            self.aviones_tierra.append(f"BOING-{numero}")
            contador += 1

    def accion(self):
        if len(self.aviones_tierra) == 0:
            return False
        else:
            accion = random.randint(0, 1)
            if accion == 0:
                return True
            else:
                return False

    def despegar_pop(self):
        if len(self.aviones_tierra) == 0:
            pass
        else:
            return self.aviones_tierra.pop(0)

    def quien_despega(self):
        if len(self.aviones_tierra) == 0:
            pass
        else:
            print("El avion que quiere despegar es el avion:", self.aviones_tierra[0])

    def estado(self):
        return self.aviones_tierra
