class Enemy:
    def __init__(self, name, age, strength, agi, con, race, damage):
        self.name = name
        self.age = age
        self.strength = strength
        self.agi = agi
        self.con = con
        self.race = race
        self.damage = damage
        self.dead = False

    def damage_recived(self, damage):
        self.con -= damage
        if self.con <= 0:
            self.dead = True

    def damage_send(self, sum_dice):
        if 2 <= sum_dice <= 4:
            self.damage += 1
        elif 5 <= sum_dice <= 7:
            self.damage += 2
        elif 8 <= sum_dice <= 10:
            self.damage += 3
        elif sum_dice == 11:
            self.damage += 4
        elif sum_dice == 12:
            self.damage += 5
        return self.damage
