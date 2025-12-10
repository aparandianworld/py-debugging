#!/usr/bin/env python3

import os
import logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler("logs/shopping.log"),
        logging.StreamHandler()
    ]  
)

logger = logging.getLogger("shopping")

def calculate_total_price(items):
    total = 0
    logging.info("Starting price calculation for %d items", len(items))

    for name, price, quantity in items:
        logging.debug("processing item %s: $%.2f  x %d", name, price, quantity)
        subtotal = price * quantity

        # bug
        if name == "banana":
            subtotal = price * quantity * 2
        total += subtotal

    tax = total * 0.10
    final_price = total + tax
    logging.info("Final price (including tax): $%.2f", final_price)
    return final_price


def main():
    shopping_cart = [
        ("apple", 2.5, 6),
        ("banana", 3.3, 6),
        ("orange", 1.5, 6),
        ("milk", 3.99, 2),
    ]

    logging.info("Shopping cart: %s", shopping_cart)
    logging.info("Items in the cart: %s", [name for name, _, _ in shopping_cart])

    try:
        total = calculate_total_price(shopping_cart)
        logging.info(f"Total is: ${total}")
    except Exception as e:
        logging.error("Error calculating total price: %s", e)

if __name__ == "__main__":
    main()
