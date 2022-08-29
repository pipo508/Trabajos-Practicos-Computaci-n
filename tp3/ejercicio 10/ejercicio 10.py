class Archivo:
    def __init__(self, nombre, extension, expresion):
        self.nombre = nombre
        self.extension = extension
        self.expresion = expresion

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def abrir_Archivo(self):
        filas = open(self.nombre + "." + self.extension, "r")
        linea = filas.readlines()
        print(linea)
        for i in linea:
            if i.strip("\n") == self.expresion:
                print(i)


expresion = str(input("ingrese la expresion deseada: "))
archivo = Archivo("archivo", "txt", expresion)
archivo.abrir_Archivo()
