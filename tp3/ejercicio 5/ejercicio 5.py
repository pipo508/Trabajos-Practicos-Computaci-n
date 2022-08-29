class Archivo:
    def __init__(self, nombre, extension, leer_o_escribir):
        self.nombre = nombre
        self.extension = extension
        self.leer_o_escribir = leer_o_escribir

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def leer_o_escribir_lineas(self):
        return open(self.nombre + "." + self.extension, self.leer_o_escribir)

    def escribir_segundo_archivo(self, filas1, filas2):
        for i in filas1:
            filas2.write(str(i))


archivo1 = Archivo("archivo1", "txt", "r")
archivo2 = Archivo("archivo2", "txt", "w")
filas1 = archivo1.leer_o_escribir_lineas()
filas2 = archivo2.leer_o_escribir_lineas()
archivo1.escribir_segundo_archivo(filas1, filas2)
