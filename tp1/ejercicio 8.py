num1=int(input("ingrese un nuemro entero"))
num2=int(input("ingrese un nuemro entero"))
menor= 0
def numero_negativo(a,b,negativo):
    if a < 0 and b < 0 :
        negativo=True
        return negativo
    elif a < 0 and b > 0 or a > 0 and b < 0:
        negativo=False
        return True
    else:
        return False
print(numero_negativo(num1,num2,menor))

