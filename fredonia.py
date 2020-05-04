from decimal import Decimal, getcontext


def time_percentage(hour: int) -> Decimal:
    return hour / Decimal('24.0')


def calculate_tax(price: str, province: str, purchased_at: int) -> Decimal:
    getcontext().prec = 2
    price = Decimal(price)
    tax_rates = {
        'Chico': Decimal('0.5'),
        'Groucho': Decimal('0.7'),
        'Harpo': Decimal('0.5'),
        'Zeppo': Decimal('0.4'),
    }

    return price + (price * tax_rates[province] * time_percentage(purchased_at))
