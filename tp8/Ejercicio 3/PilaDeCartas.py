class PilaDeCartas:
    def __init__(self):
        self.pila = []

    def apilar(self, carta):
        if len(self.pila) <= 0:
            self.pila.append(carta)
        else:
            ultima_carta = self.pila[-1]

            if ultima_carta.palo != carta.palo and ultima_carta.valor - 1 == carta.valor:
                self.pila.append(carta)
            elif ultima_carta.palo != carta.palo and ultima_carta.valor - 1 != carta.valor:
                print(f"ERROR VALOR[ULTIMA CARTA: {ultima_carta.valor}, CARTA ENTRANTE: {carta.valor}")
            elif ultima_carta.palo == carta.palo and ultima_carta.valor - 1 == carta.valor:
                print(f"ERROR PALO[ULTIMA CARTA: {ultima_carta.palo}, CARTA ENTRANTE: {carta.palo}")

    def __str__(self):
        return f"Estado actual de la pila: {self.pila}"


