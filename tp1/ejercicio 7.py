numero_ingresado=int(input("ingrese un numero entero"))
valor_absoluto=abs(numero_ingresado)
print(valor_absoluto)
def cerca_cien(a):
    if a >= 90 and a < 100:
        return True
    else:
        return False
print(cerca_cien(numero_ingresado))
