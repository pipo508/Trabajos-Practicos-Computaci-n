class Archivo:
    def __init__(self, nombre, extension):
        self.nombre = nombre
        self.extension = extension

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def guardar_lineas(self):
        filas = open(self.nombre + "." + self.extension, "r")
        for i in filas:
            list.append(i.strip("\n"))


list = []
archivo = Archivo("archivo", "txt")
archivo.guardar_lineas()
print(list)
