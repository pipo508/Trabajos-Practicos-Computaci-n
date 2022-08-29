num1= int(input("ingrese un numero entero"))
num2= int(input("ingrese un numero entero"))
def sum(a , b):
    if a == b:
        suma=a+b
        sum2 = suma + suma
        return sum2
    else:
        suma= a+b
        return suma
print(sum(num1 , num2))
