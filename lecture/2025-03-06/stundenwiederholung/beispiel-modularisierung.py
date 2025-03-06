# Wie müsste man das folgende Python Programm modularisieren, sodass die Programmteile wie folgt 
# verwendet werden können.

# Programm 1 - Lotto
from game.lotto import spiel_lotto_vereinfacht
from ausgabe.screen import ausgabe_lotto

zahlen = spiel_lotto_vereinfacht()
ausgabe_lotto(zahlen)

# Programm 2 - Joker
from game.joker import spiel_jocker
from ausgabe.screen import ausgabe_jocker

zahlen = spiel_joker()
ausgabe_joker(zahlen)


### Ursprüngliches Programm

from random import randint

def ausgabe_lotto(zahlen):
    lotto_zahlen, glueckszahl = zahlen
    print("Die Lottozahlen lauten:", ", ".join(lotto_zahlen))
    print("Glückszahl:", glueckszahl)

def ausgabe_joker(zahlen):
    print("Die Jokerzahlen lauten:", zahlen) 

def spiel_lotto_vereinfacht():
    """
    Ermitteln der Lotto Zahlen
    """
    lotto_zahlen = []
    for _ in range(6):
        lotto_zahlen.append(str(randint(1, 42)))
    glueckszahl = randint(1, 6)
    return lotto_zahlen, glueckszahl

def spiel_joker():
    """
    Ermitteln der Joker Zahl
    """
    jocker = randint(0,999999)
    return f"{jocker:06d}"      # führende Nullen ausgeben

if __name__ == '__main__':
    zahlen = spiel_lotto_vereinfacht()
    ausgabe_lotto(zahlen)
    print("---")
    zahlen = spiel_joker()
    ausgabe_joker(zahlen)

