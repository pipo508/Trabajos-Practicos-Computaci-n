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
        for i in filas.readlines()[0:self.num_lineas]:
            print(i)


nombre_archivo = str(input("escriba el nombre del archivo: "))
ext = str(input("ingrese la extension: "))
num = int(input("ingrese la cantidad de lineas que desea leer: "))
archivo = Archivo(nombre_archivo, ext, num)
archivo.abrir_Archivo()
