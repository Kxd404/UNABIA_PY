# billing.py - calculates the total and the discount

def calculate_total(orders):
    total = 0

    for item_code in orders:
        quantity = orders[item_code][1]
        item_price = orders[item_code][2]
        item_total = quantity * item_price
        total = total + item_total

    return total


def calculate_discount(total):
    if total >= 1000:
        discount = total * 0.10
    elif total >= 500:
        discount = total * 0.05
    else:
        discount = 0

    return discount
