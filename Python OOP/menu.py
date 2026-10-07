# menu.py - Menu class: owns the menu items and how they are shown


class Menu:

    def __init__(self):
        self.items = {
            "1": ["Cheeseburger", 85],
            "2": ["Chicken Meal", 120],
            "3": ["French Fries", 55],
            "4": ["Spaghetti", 95],
            "5": ["Soft Drink", 40]
        }

    def has_item(self, item_code):
        return item_code in self.items

    def get_name(self, item_code):
        return self.items[item_code][0]

    def get_price(self, item_code):
        return self.items[item_code][1]

    def print_menu(self):
        print()
        print("-" * 45)
        print("                   MENU")
        print("-" * 45)
        print("{:<8} {:<25} {:>10}".format("CODE", "ITEM", "PRICE"))

        for item_code in self.items:
            print("{:<8} {:<25} ₱{:>9,.2f}".format(
                item_code, self.get_name(item_code), self.get_price(item_code)
            ))

        print("-" * 45)
