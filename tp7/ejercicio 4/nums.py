class Bingo:
    def formar_palabra(self, lista_nums):
        list_1 = []
        for i in lista_nums:
            if i == 2 or i == 9 or i == 14 or i == 7 or i == 15:
                list_1.append(i)
        if 2 in list_1 and 9 in list_1 and 14 in list_1 and 7 in list_1 and 15 in list_1:
            return "WIN"
        else:
            return "LOSE"
