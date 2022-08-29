def getIndices(listNumber, number):
    return [i for i, x in enumerate(listNumber) if x == number]


list = []
print(getIndices(list, 3))
