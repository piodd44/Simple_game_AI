# Simple_game_AI

Proste Ai które jest w stanie grać w gry kombinatoryczne używając algorytmu min_max//
Algorytm jest zoptymalizowany pod kontem nie rozpatrywania wielokrotnie tej samej pozycji powstałej przez rózne sekwencje ruchów//


Aby działał porprawnie należy zapewnić aby gra "podpieta" pod AI //
posiadała funkcje które://
(rozrzeszała classe Position,Game)//
-jeśli są ostatnią pozycją w grze dają ocene 1 jeśli wygrał gracz 1 , -1 jeśli wygrał gracz 2 , 0 jeśli remis//
-zwraca wszystkie legalne ruchy w pozycji //
-zwraca pozycje po wykonaniu danego ruchu //
-zwraca nr_gracza który jest w danym momecie na ruchu //
-zwraca klucz jednoznacznie identyfikujacy dana pozycjie ( nr_gracza który jest na ruchu jest cześcią pozycji ) //

