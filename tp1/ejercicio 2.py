monoA_input=input("el mono a esta sonriendo")
monoB_input=input("el mono B esra sonriendo")
if monoA_input == "si":
    monoA_input = True
else:
    monoA_input= False
if monoB_input == "si":
    monoB_input= True
else:
    monoB_input=False
def monos_funtion(mmonoA , monoB):
    if (mmonoA == True and monoB == True) or (mmonoA == False and monoB == False) :
        return True
    else:
        return False
print(monos_funtion(monoA_input,monoB_input))

