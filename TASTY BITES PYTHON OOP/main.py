# main.py - asks the customer for input and uses the Menu and Order objects

from menu import Menu
from order import Order


def print_header():
    print()
    print("=" * 45)
    print("          WELCOME TO TASTY BITES")
    print("=" * 45)


def ask_yes_no(question):
    answer = input(question).lower()
    return answer == "yes" or answer == "y"


def get_menu_item(menu):
    item_code = input("Enter item code: ")

    if menu.has_item(item_code):
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


def main():
    menu = Menu()
    order = Order(menu)

    print_header()
    menu.print_menu()

    if ask_yes_no("Would you like to order? (yes/no): "):
        ordering = True

        while ordering:
            item_code = get_menu_item(menu)

            if item_code != "":
                quantity = get_quantity()

                if quantity > 0:
                    order.add_item(item_code, quantity)
                    ordering = ask_yes_no("Would you like to order another item? (yes/no): ")
            else:
                print("Please choose a valid menu item.")

        if not order.is_empty():
            order.print_receipt()
        else:
            print("No items were ordered.")
    else:
        print()
        print("Thank you for visiting Tasty Bites!")
        print("Have a nice day!")


if __name__ == "__main__":
    main()
