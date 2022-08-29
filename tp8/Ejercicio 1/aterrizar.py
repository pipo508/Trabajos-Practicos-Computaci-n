import random


class Aterrizar:
    aviones_volando = []

    def push_aviones_volando(self, cantidad):
        contador = 0
        while contador < cantidad:
            numero = random.randint(100, 999)
            self.aviones_volando.append(f"BOING-{numero}")
            contador += 1

    def accion(self):
        if len(self.aviones_volando) == 0:
            return False
        else:
            accion = random.randint(0, 1)
            if accion == 0:
                return True
            else:
                return False

    def aterrizar_pop(self):
        if len(self.aviones_volando) == 0:
            pass
        else:
            return self.aviones_volando.pop(0)

    def quien_Aterriza(self):
        if len(self.aviones_volando) == 0:
            pass
        else:
            print("El avion que quiere aterrizar es el avion:", self.aviones_volando[0])

    def estado(self):
            return self.aviones_volando
