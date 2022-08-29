class Archivo:
    def __init__(self, nombre, extension, num_lineas):
        self.nombre = nombre
        self.extension = extension
        self.num_lineas = num_lineas

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def abrir_Archivo(self):
        filas = open(self.nombre + "." + self.extension, "r")
        print(filas.readlines()[0:self.num_lineas])


num = int(input("ingrese la cantidad de lineas que desea leer: "))
archivo = Archivo("archivo", "txt", num)
archivo.abrir_Archivo()
