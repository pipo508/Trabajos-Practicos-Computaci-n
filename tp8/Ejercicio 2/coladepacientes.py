RED = '\033[31m'
RESET = '\033[39m'
class Cola_pacientes:
    cola_pacientes = []

    def nuevo_paciente(self, paciente):
        self.cola_pacientes.append(paciente)
        print(f"El paciente {paciente} se agregó correctamente")

    def proximo_paciente(self):
        if len(self.cola_pacientes) == 0:
            pass
        else:
            print(f"El proximo paciente es :  {self.cola_pacientes[0]}")

    def sacar_paciente(self):
        if len(self.cola_pacientes) == 0:
            pass
        else:
            self.cola_pacientes.pop(0)

    def llamar_paciente(self):
        if len(self.cola_pacientes) == 0:
            print(f"{RED}\nNo hay pacientes en espera")
            print(RESET)
        else:
            print(f"Ingresa el paciente:{self.cola_pacientes[0]} ")

    def eliminar_paciente(self):
        if len(self.cola_pacientes) == 0:
            print(f"{RED}\nNo hay pacientes en la lista")
            print(RESET)
        else:
            while True:
                print("Ingrese el nombre del paciente que desea eliminar")
                nombre = str(input("Nombre:"))
                estado = nombre in self.cola_pacientes
                if estado is True:
                    indice = self.cola_pacientes.index(nombre)
                    self.cola_pacientes.pop(indice)
                    print(f"{RED}El paciente fue eliminado de la lista")
                    print(RESET)
                    break
                else:
                    print(f"{RED}\nEl paciente no se encuéntra")
                    print(RESET)