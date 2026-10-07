# ordering.py - asks the customer for input and builds the order

from menu import menu


def ask_to_order():
    answer = input("Would you like to order? (yes/no): ").lower()

    if answer == "yes" or answer == "y":
        return True
    else:
        return False


def get_menu_item():
    item_code = input("Enter item code: ")

    if item_code in menu:
        return item_code
    else:
        print("Invalid item code.")
        return ""


def get_quantity():
    quantity_text = input("Enter quantity: ")

    if quantity_text.isdigit():
        quantity = int(quantity_text)

        if quantity > 0:
            return quantity
        else:
            print("Quantity must be greater than zero.")
            return 0
    else:
        print("Invalid quantity.")
        return 0


def add_order(orders, item_code, quantity):
    item_name = menu[item_code][0]
    item_price = menu[item_code][1]

    if item_code in orders:
        orders[item_code][1] = orders[item_code][1] + quantity
    else:
        orders[item_code] = [item_name, quantity, item_price]


def ask_for_another_item():
    answer = input("Would you like to order another item? (yes/no): ").lower()

    if answer == "yes" or answer == "y":
        return True
    else:
        return False
