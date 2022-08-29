from coladepacientes import Cola_pacientes

RED = '\033[31m'
RESET = '\033[39m'

cola_pacientes = Cola_pacientes()
while True:
    print("Escoja la opcion que desea realizar: \n 1:Agregar paciente \n 2:Borrar paciente \n 3:Llamar paciente")
    opcion = int(input("Su opcion: "))
    if opcion == 1:
        nombre = str(input("Ingrese el nombre del paciente que desea agregar: "))
        cola_pacientes.nuevo_paciente(nombre)
    elif opcion == 2:
        cola_pacientes.eliminar_paciente()
    elif opcion == 3:
        cola_pacientes.llamar_paciente()
        cola_pacientes.sacar_paciente()
        cola_pacientes.proximo_paciente()
    else:
        print(f"{RED}\nSu opcion no se encuentra en las opciones")
        print(RESET)
