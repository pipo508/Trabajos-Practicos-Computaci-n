class Archivo:
    def __init__(self, nombre, extension):
        self.nombre = nombre
        self.extension = extension
        self.lineas = list()

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def contador_lineas(self):
        filas = open(self.nombre + "." + self.extension, "r")
        self.lineas = filas.readlines()
        print("la cantidad de filas es:", len(self.lineas))

    def contador_palabras(self):
        contador = 0
        for i in self.lineas:
            contador = contador + len(i.split())
        print("la cantidad de palabras es:", contador)

    def contador_caracteres(self):
        contador = 0
        for i in self.lineas:
            for j in i.split():
                contador = contador + len(j)
        print("la cantidad de caracteres es:",contador)

archivo = Archivo("archivo", "txt")
archivo.contador_lineas()
archivo.contador_palabras()
archivo.contador_caracteres()
