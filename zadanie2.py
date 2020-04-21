#!/usr/bin/env python
import sys


RATES = {  # From www.xe.com (3.04.2020 17:10)
        ('eur', 'pln'): 4.57,
        ('pln', 'eur'): 0.22,
        ('usd', 'pln'): 4.20,
        ('pln', 'usd'): 0.24,
        ('eur', 'usd'): 1.08,
        ('usd', 'eur'): 0.93,
    }


def parse_input(args):
    """Parse input from `args` (list) into appropriate data types."""
    try:
        from_currency = args[1].lower()
        to_currency = args[2].lower()
        amount = float(args[3])
        if from_currency not in {'pln', 'usd', 'eur'} or to_currency not in {'pln', 'usd', 'eur'}:
            raise ValueError
    except (IndexError, ValueError) as error:
        print("Error! Usage:\n\n" \
            "\t./currency_exchange.py FROM_CURRENCY TO_CURRENCY AMOUNT\n\n" \
            "FROM_CURRENCY and TO_CURRENCY must one of {'pln', 'usd', 'eur'} and AMOUNT must a number.", 
            file=sys.stderr)
        sys.exit(1)
    return from_currency, to_currency, amount


def calculate_exchange(from_currency, to_currency, amount, rates=RATES):
    """Calculate return amount exchanging `value` given in `from_currency` into value in `to_currency`."""
    if from_currency == to_currency:
        return_amount = amount
    else:
        return_amount = RATES[(from_currency, to_currency)] * amount
    return return_amount


if __name__ == "__main__":
    from_currency, to_currency, amount = parse_input(sys.argv)
    return_amount = calculate_exchange(from_currency, to_currency, amount)
    print("Amount after conversion: " + str(return_amount) + " " + to_currency.upper())
