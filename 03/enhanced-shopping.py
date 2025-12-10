#!/usr/bin/env python3

import os
from loguru import logger

os.makedirs("logs", exist_ok=True)
logger.add(
    "logs/shopping.log",
    format="{time:%H:%M:%S} | {level: <8} | {message}",
    level="DEBUG",
)
logger.add(
    lambda msg: print(msg, end=""),
    format="{time:%H:%M:%S} | {level: <8} | {message}",
    level="DEBUG",
)


def calculate_total_price(items):
    total = 0
    logger.info("Starting price calculation for {} items", len(items))

    for name, price, quantity in items:
        logger.debug("processing item {}: ${:.2f}  x {}", name, price, quantity)
        subtotal = price * quantity

        # bug
        if name == "banana":
            subtotal = price * quantity * 2
        total += subtotal

    tax = total * 0.10
    final_price = total + tax
    logger.info("Final price (including tax): ${:.2f}", final_price)
    return final_price


def main():
    shopping_cart = [
        ("apple", 2.5, 6),
        ("banana", 3.3, 6),
        ("orange", 1.5, 6),
        ("milk", 3.99, 2),
    ]

    logger.info("Shopping cart: {}", shopping_cart)
    logger.info("Items in the cart: {}", [name for name, _, _ in shopping_cart])

    try:
        total = calculate_total_price(shopping_cart)
        logger.info(f"Total is: ${total}")
    except Exception as e:
        logger.error("Error calculating total price: {}", e)


if __name__ == "__main__":
    main()
