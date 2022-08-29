loro=str(input("el loro esta hablando"))
rango=int(input("ingrese una hora entre las 0 y las 23"))
if loro == "si":
    loro= True
else:
    loro= False
if rango < 0 or rango > 23:
    print("ingrese una hora corresppondiente")
def hablando(loro,hora):
    if (loro == True) and (hora < 7 or hora > 20):
        return True
    elif (loro == True) and hora >= 7 or hora <= 20:
        return False
    else:
        return False
print(hablando(loro, rango))

