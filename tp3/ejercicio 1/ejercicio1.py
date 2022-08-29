class Archivo:
    def __init__(self, nombre, extension):
        self.nombre = nombre
        self.extension = extension

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def abrir_Archivo(self):
        filas = open(self.nombre + "." + self.extension, "r")
        print(filas.readlines())


archivo = Archivo("archivo", "txt")
archivo.abrir_Archivo()
