from os import rename, scandir, path, mkdir
import shutil

originPathDirectory = 'C:/Users/Verdini/Desktop/2do año/computacion'
destinationPathDirectory = 'C:/Users/Verdini/Desktop/2do año/computacion/tp2'

# creamos un nuevo directorio y si ya existe lo borramos antes
if path.exists(destinationPathDirectory):
	shutil.rmtree(destinationPathDirectory)

mkdir(destinationPathDirectory)

# en esta línea scandir busca todos los elementos del directorio 
# que le pasemos, arma una lista y lo asigna a la variable files
files = scandir(originPathDirectory)

# este tipo de for itera sobre todos los elementos de la lista files y a cada elemento 
# lo pone en la variable file que va cambiando con cada iteración
number = 1
for file in files:
	if file.is_file():
		# path.splittext separa y guarda en un array el nombre del archivo (en la posición 0) y la extensión (en la posición 1)
		# nosotros usamos el [1] para tomar la segunda posición, donde está la extensión
		name = path.splitext(file.name)[0]
		extension = path.splitext(file.name)[1] 

		# creamos un nuevo nombre eliminando los digitos, para ello iteramos sobre los caracteres del nombre y sólo 
		# nos quedamos con los que no son números
		newName = ""
		for c in name:
			if not c.isdigit():
				newName += c

		# renombramos el archivo, para eso usamos la función rename(archivo_original, nuevo_archivo) 
		# pero tenemos que pasar la ruta completa, por eso usamos path.join(directorio, nombre_archivo)
		rename(path.join(originPathDirectory, file.name), path.join(destinationPathDirectory, newName + extension)) 

		# finalmente incrementamos el valor de number
		number = number + 1 
