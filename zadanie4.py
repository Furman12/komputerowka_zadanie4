#!/usr/bin/env python
import sys

ERROR_ZERO_ARGS = """Nie podałeś argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi."""

ERROR_FEW_ARGS = """
Za mało argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
"""

ERROR_MANY_ARGS = """
Za dużo argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
"""

ERROR_WRONG_TYPES = """
Złe typy argumentów. Sposób użycia:

   ./zadanie4.py a q N

Program wylicza kolejne sumy częściowe szeregu geometrycznego.
N powinno być liczbą naturalną, a oraz q liczbami rzeczywistymi.
"""

def parse_input(args):
    """Parse input from `args` (list) into appropriate data types."""
    try:
        a = float(args[1])
        q = float(args[2])
        N = int(args[3])
    except ValueError as error:
        print(ERROR_WRONG_TYPES)
        sys.exit(1)
    except IndexError as error:
        if len(args) == 1:
            print(ERROR_ZERO_ARGS)
        elif len(args) < 3:
            print(ERROR_FEW_ARGS)
        elif len(args) > 4:
            print(ERROR_MANY_ARGS)
        sys.exit(1)
    return a, q, N


def calculate_sum(a, q, n):
    S = (a*(q**n - 1))/(q-1)
    return S

def calculate_series(a, q, N):
    return [calculate_sum(a=a,q=q,n=n) for n in range(1,N+1)]

def print_results(l):
    for elem in l:
        print(elem)

if __name__ == "__main__":
    a, q, N = parse_input(sys.argv)
    sums = calculate_series(a,q,N)
    print_results(sums)

