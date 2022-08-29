class Archivo:
    def __init__(self, nombre, extension, delimitador):
        self.nombre = nombre
        self.extension = extension
        self.delimitador = delimitador
        self.texto = ""

    def get_nombre(self):
        return (self.nombre)

    def get_extension(self):
        return (self.extension)

    def abrir_Archivo(self):
        filas = open(self.nombre + "." + self.extension, "r")
        self.texto = filas.readline()
        texto_delimitado = self.texto.replace(" ", delimitador)
        print(texto_delimitado)


nombre_archivo = str(input("escriba el nombre del archivo: "))
ext = str(input("ingrese la extension: "))
delimitador = str(input("ingrese un delimitador: "))
archivo = Archivo(nombre_archivo, ext, delimitador)
archivo.abrir_Archivo()
