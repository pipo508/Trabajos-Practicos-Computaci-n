num1= int(input("ingrese el numero"))
num2= 21
def diferencia(a,b):
    if a > b :
        resta= a-b
        resta2= resta + resta
        return abs(resta2)
    else:
        resta= a-b
        return abs(resta)
print(diferencia(num1,num2))
