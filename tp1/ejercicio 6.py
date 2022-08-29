num1=int(input("ingrese un valor entero"))
num2=int(input("ingrese un valor entero"))
def num10(a,b):
    if (a+b) == 10:
        return True
    elif ( a or b ) == 10:
       return True
    else:
        return False
print(num10(num1,num2))
