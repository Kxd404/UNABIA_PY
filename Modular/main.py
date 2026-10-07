# main.py - runs the program by calling the functions from the other files

from display import print_header, print_menu, print_receipt
from ordering import (ask_to_order, get_menu_item, get_quantity,
                      add_order, ask_for_another_item)


def main():
    orders = {}

    print_header()
    print_menu()

    if ask_to_order():
        ordering = True

        while ordering:
            item_code = get_menu_item()

            if item_code != "":
                quantity = get_quantity()

                if quantity > 0:
                    add_order(orders, item_code, quantity)
                    ordering = ask_for_another_item()
            else:
                print("Please choose a valid menu item.")

        if len(orders) > 0:
            print_receipt(orders)
        else:
            print("No items were ordered.")
    else:
        print()
        print("Thank you for visiting Tasty Bites!")
        print("Have a nice day!")


if __name__ == "__main__":
    main()
