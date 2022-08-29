class Sum:
    def __init__(self):
        self.list_1 = []

    def enter_numbers(self, index):
        for i in range(0, index):
            num = int(input("Enter the number you want to use: "))
            self.list_1.append(num)
        self.list_1.sort(reverse=True)
        print(self.list_1)

    def sum_numbers(self, nombre=0):
        array = []
        if nombre == 0:
            array = self.list_1
        else:
            array = nombre
        suma = 0
        array = [7, 6, 5]
        for i in range(0, len(array) - 1):
            suma += array[i] - (array[i + 1])
        print("The sum of the difference of the chosen numbers is:", suma)
        return suma



