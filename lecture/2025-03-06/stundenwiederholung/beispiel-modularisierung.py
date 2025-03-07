# Wie müsste man das folgende Python Programm modularisieren, sodass die Programmteile wie folgt 
# verwendet werden können.

# Programm 1 - Lotto
from game.lotto import spiel_lotto_vereinfacht
from ausgabe.screen import ausgabe_lotto

zahlen = spiel_lotto_vereinfacht()
ausgabe_lotto(zahlen)

# Programm 2 - Joker
from game.joker import spiel_joker
from ausgabe.screen import ausgabe_joker

zahlen = spiel_joker()
ausgabe_joker(zahlen)
