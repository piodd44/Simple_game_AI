# Simple_game_AI

Proste Ai które jest w stanie grać w gry kombinatoryczne używając algorytmu min_max <br>
Algorytm jest zoptymalizowany pod kontem nie rozpatrywania wielokrotnie tej samej pozycji powstałej przez rózne sekwencje ruchów<br>
<br>
<br>
Aby działał porprawnie należy zapewnić aby gra "podpieta" pod AI rozrzeszała classe Position,Game <br>
czyli posiadała funkcje które:<br>

-koncowym pozycją w grze dają ocene 1 jeśli wygrał gracz 1 , -1 jeśli wygrał gracz 2 , 0 jeśli remis <br>
-zwraca wszystkie legalne ruchy w pozycji <br>
-zwraca pozycje po wykonaniu danego ruchu <br>
-zwraca nr_gracza który jest w danym momecie na ruchu <br>
-zwraca klucz jednoznacznie identyfikujacy dana pozycjie ( nr_gracza który jest na ruchu jest cześcią pozycji )<br>

