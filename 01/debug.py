#!/usr/bin/env python3

# import pdb


def calculate_total_price(items):
    total = 0
    for name, price, quantity in items:
        print(f"processing {name}: ${price} * {quantity}")
        subtotal = price * quantity

        # bug
        if name == "banana":
            subtotal = price * quantity * 2
        total += subtotal

    tax = total * 0.10
    return total + tax


def main():
    shopping_cart = [
        ("apple", 2.5, 6),
        ("banana", 3.3, 6),
        ("orange", 1.5, 6),
        ("milk", 3.99, 2),
    ]

    # pdb.set_trace()
    total = calculate_total_price(shopping_cart)
    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
