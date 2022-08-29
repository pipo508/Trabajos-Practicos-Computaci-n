def caracter_perdido(str,n):
    if n or n == 0:
        mitad1 = str[:n]
        mitad2 = str[n+1:]
        return mitad1 + mitad2
    elif n == -1:
        return str[:-1]
cadena = str(input("Ingrese una palabra: "))
indice = int(input("Ingrese un indice: "))
print(caracter_perdido(cadena,indice))