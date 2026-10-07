# order.py - Order class: owns the customer's items, total, discount and receipt


class Order:

    def __init__(self, menu):
        self.menu = menu
        self.items = {}

    def add_item(self, item_code, quantity):
        if item_code in self.items:
            self.items[item_code][1] = self.items[item_code][1] + quantity
        else:
            self.items[item_code] = [
                self.menu.get_name(item_code),
                quantity,
                self.menu.get_price(item_code)
            ]

    def is_empty(self):
        return len(self.items) == 0

    def calculate_total(self):
        total = 0

        for item_code in self.items:
            quantity = self.items[item_code][1]
            item_price = self.items[item_code][2]
            total = total + quantity * item_price

        return total

    def calculate_discount(self):
        total = self.calculate_total()

        if total >= 1000:
            discount = total * 0.10
        elif total >= 500:
            discount = total * 0.05
        else:
            discount = 0

        return discount

    def print_receipt(self):
        total = self.calculate_total()
        discount = self.calculate_discount()
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

        for item_code in self.items:
            item_name = self.items[item_code][0]
            quantity = self.items[item_code][1]
            item_price = self.items[item_code][2]
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
