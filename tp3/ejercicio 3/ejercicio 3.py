class Archivo:
    def __init__(self, nombre, extension, text):
        self.nombre = nombre
        self.extension = extension
        self.text = text

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def escribir_Archivo(self):
        filas = open(self.nombre + "." + self.extension, "w")
        filas.write(self.text)


text = str(input("ingrese le texto que quiere agregar al archivo: "))
archivo = Archivo("archivo", "txt", text)
archivo.escribir_Archivo()
