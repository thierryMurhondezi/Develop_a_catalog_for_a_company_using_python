def calculate_total_price(item1, item2, item3):
    # Initialize variables for individual price, combo discount, and gift discount
    individual_price = 200
    combo_discount = 400
    gift_discount = 600

    # Initialize total price variable
    total_price = 0

    # Calculate total price based on combination of items
    if item1 and item2 and item3:
        # If all three items are purchased, multiply individual price by 3 and apply gift discount
        total_price = individual_price * 3 * (1 - gift_discount)
    elif item1 and item2:
        # If only two items are purchased, multiply individual price by 2 and apply combo discount
        total_price = individual_price * 2 * (1 - combo_discount)
    elif item1 or item2 or item3:
        # If only one item is purchased, total price is the individual price
        total_price = individual_price

    # Return the calculated total price
    return total_price


# Test cases
print(calculate_total_price(True, True, True))  # Expected output: 22.5 (3 items with gift discount)
print(calculate_total_price(True, True, False))  # Expected output: 18.0 (2 items with combo discount)
print(calculate_total_price(True, False, False))  # Expected output: 10.0 (1 item)
print(calculate_total_price(False, False, False))  # Expected output: 0.0 (no items)
