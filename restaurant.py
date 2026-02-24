def display_menu(menu):
    print("\n========== MENU ==========")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item} - ₹{price}")


def take_order(menu):
    order = {}
    total_bill = 0

    while True:
        item_name = input("\nEnter item name to order (or type 'done' to finish): ").strip()

        if item_name.lower() == "done":
            break

        found = False

        for category, items in menu.items():
            if item_name in items:
                try:
                    quantity = int(input("Enter quantity: "))
                    cost = items[item_name] * quantity
                    total_bill += cost

                    if item_name in order:
                        order[item_name] += quantity
                    else:
                        order[item_name] = quantity

                    print(f"{item_name} added to order. Cost: ₹{cost}")
                    found = True
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
                break

        if not found:
            print("Item not found in menu. Please try again.")

    return order, total_bill


def print_bill(order, total_bill):
    print("\n========== BILL ==========")
    for item, quantity in order.items():
        print(f"{item} x {quantity}")
    print("--------------------------")
    print(f"Total Bill: ₹{total_bill}")
    print("Thank you for visiting!")


def main():
    menu = {
        "Starters": {
            "Spring Rolls": 100,
            "Garlic Bread": 80
        },
        "Main Course": {
            "Paneer Butter Masala": 180,
            "Veg Biryani": 150
        },
        "Desserts": {
            "Gulab Jamun": 50,
            "Ice Cream": 60
        },
        "Drinks": {
            "Water Bottle": 20,
            "Lassi": 40
        }
    }

    print("Welcome to Our Restaurant!")
    display_menu(menu)
    order, total_bill = take_order(menu)
    print_bill(order, total_bill)


if __name__ == "__main__":
    main()