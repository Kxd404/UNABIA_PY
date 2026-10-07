# display.py - everything that is printed to the screen

from menu import menu
from billing import calculate_total, calculate_discount


def print_header():
    print()
    print("=" * 45)
    print("          WELCOME TO TASTY BITES")
    print("=" * 45)


def print_menu():
    print()
    print("-" * 45)
    print("                   MENU")
    print("-" * 45)
    print("{:<8} {:<25} {:>10}".format("CODE", "ITEM", "PRICE"))

    for item_code in menu:
        item_name = menu[item_code][0]
        item_price = menu[item_code][1]
        print("{:<8} {:<25} ₱{:>9,.2f}".format(
            item_code, item_name, item_price
        ))

    print("-" * 45)


def print_receipt(orders):
    total = calculate_total(orders)
    discount = calculate_discount(total)
    final_total = total - discount

    print()
    print("=" * 55)
    print("                 TASTY BITES")
    print("              OFFICIAL RECEIPT")
    print("=" * 55)
    print("{:<20} {:>5} {:>12} {:>12}".format(
        "ITEM", "QTY", "PRICE", "TOTAL"
    ))
    print("-" * 55)

    for item_code in orders:
        item_name = orders[item_code][0]
        quantity = orders[item_code][1]
        item_price = orders[item_code][2]
        item_total = quantity * item_price

        print("{:<20} {:>5} ₱{:>10,.2f} ₱{:>10,.2f}".format(
            item_name, quantity, item_price, item_total
        ))

    print("-" * 55)
    print("{:<40} ₱{:>10,.2f}".format("SUBTOTAL:", total))
    print("{:<40} ₱{:>10,.2f}".format("DISCOUNT:", discount))
    print("{:<40} ₱{:>10,.2f}".format("TOTAL:", final_total))
    print("=" * 55)
    print("       Thank you for ordering at Tasty Bites!")
    print("=" * 55)
