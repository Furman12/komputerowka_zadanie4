echo "Skrypt wylicza ilość waluty na podstaie zadanego kursu. 
Skrypt przyjmuje nazwę waluty którą sprzedajemy jako pierwszy argument, 
nazwę waluty którą chcemy kupić jako drugi argument 
oraz ilość jako trzeci argument.

Funkcja parse_input pobiera argumenty od użytkownika i sprawdza ich poprawność i wywołuje ValueError w razie błędnych argumentów.

Funkcja calculate_exchange oblicza ilość wymienionej waluty.

Skrypt na podstawie wyej wymienionych funkcji oblicza i wyśietla ilość waluty którą chcemy kupić."

echo "Prawidłowy przykład użycia"
echo '$python3 zadanie2.py pln eur 100'
python3 zadanie2.py pln eur 100

echo 'Nieprawidłowy przykład użycia'
echo '$python3 zadanie2.py pln gbp 100'
python3 zadanie2.py pln gbp 100

echo 'Dziwny przykład użycia'
echo '$python3 zadanie2.py usd pln -200'
python3 zadanie2.py usd pln -200