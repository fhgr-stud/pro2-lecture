from random import randint

def spiel_joker():
    """
    Ermitteln der Joker Zahl
    """
    jocker = randint(0,999999)
    return f"{jocker:06d}"      # führende Nullen ausgeben