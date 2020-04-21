# Komputerówka – 22.04.2020

## Zadanie 1

Utwórz plik `zadanie1.txt` i opisz swoimi słowami działanie komendy `find`.
W opisie umieść minimum trzy przykłady użycia z opisem przykładowej sytuacji,
w której mógłbyś chcieć skorzystać z tej komendy.

Pamiętaj wgrać plik `zadanie1.txt` na serwer.

## Zadanie 2

Otwórz skrypt `zadanie2.py`. Przeczytaj kod i spróbuj go uruchomić.
Utwórz plik `zadanie2.sh` będący skryptem w powłoce BASH. W skrypcie umieść:

  - opis działania komendy w komentarzach,
  - trzy przykładowe, działające użycia komendy dla różnych argumentów.

Pamiętaj wgrać plik `zadanie2.sh` na serwer.

## Zadanie 3

Napisz skrypt o nazwie `zadanie4.py`, napisany w języku Python. Skrypt powinien
obliczać kolejne sumy częściowe szeregu geometrycznego. Postaraj się zadbać
o to, program działał również dla błędnych wartości podanych przez użytkownika.

Skrypt powinien mieć funkcje:

  - `parse_input(args)`, której przekazujemy argumenty wczytane z linii komend
    a w wyniku, zwraca trzy liczby: `a`, `q` oraz `N`;
  - `calculate_sum(a, q, n)`, która wylicza wartości sumy częściowej pierwszych
    `n` wyrazów szeregu geometrycznego o pierwszym wyrazie `a` i ilorazie `q`;
  - `calculate_series(a, q, N)`, która wylicza wartości sumy częściowej dla `n`
    równego od `1` do `N`, wyniki zapisz w postaci listy liczb;
  - `print_results(l)`, która wypisuje na ekranie wyniki linia pod linijką
    w odpowiedniej postaci (spójrz na przykładowe wywołanie poniżej).

Przykład 1:

```
[student@komputer zadanie]$ ./zadanie4.py 2 1.5 10
2.0
5.0
9.5
16.25
26.375
41.5625
64.34375
98.515625
149.7734375
226.66015625
```

Przykład 2:

```
[student@komputer zadanie]$ ./zadanie4.py
Nie podałeś argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
```

Przykład 3:

```
[student@komputer zadanie]$ ./zadanie4.py 2 1
Za mało argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
```

Przykład 4:

```
[student@komputer zadanie]$ ./zadanie4.py 2 1 2 1
Za dużo argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
```

Przykład 5:

```
[student@komputer zadanie]$ ./zadanie4.py 2 1 1.5
Złe typy argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
```
