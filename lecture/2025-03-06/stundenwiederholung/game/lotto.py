from random import randint

def spiel_lotto_vereinfacht():
    """
    Ermitteln der Lotto Zahlen
    """
    lotto_zahlen = []
    for _ in range(6):
        lotto_zahlen.append(str(randint(1, 42)))
    glueckszahl = randint(1, 6)
    return lotto_zahlen, glueckszahl

