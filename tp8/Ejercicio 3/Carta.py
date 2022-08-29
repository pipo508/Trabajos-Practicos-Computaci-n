import random


class Carta:
    def __init__(self):
        self.palo = random.choice(["Espada", "Basto", "Oro", "Copa"])
        self.valor = random.randint(1, 12)

    def __repr__(self):
        return f'Palo: {self.palo}, Valor: {self.valor}'

    def __str__(self):
        return f"Palo: {self.palo}, Valor: {self.valor}"
