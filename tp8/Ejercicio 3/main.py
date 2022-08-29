from Carta import Carta
from PilaDeCartas import PilaDeCartas


def main():
    pila_de_cartas = PilaDeCartas()

    for i in range(10):
        carta = Carta()
        pila_de_cartas.apilar(carta)
        print(pila_de_cartas)


if __name__ == '__main__':
    main()
