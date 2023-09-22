def calculate_price():
    items = {
        "Item 1": 200.0,
        "Item 2": 400.0,
        "Item 3": 600.0
    }
    
    combos = {
        "Combo 1(Item 1+2)": ["Item 1", "Item 2"],
        "Combo 2(Item 2+3)": ["Item 2", "Item 3"],
        "Combo 3(Item 1+3)": ["Item 1", "Item 3"],
        "Combo 4(Item 1+2+3)": ["Item 1", "Item 2", "Item 3"]
    }
    
    total_price = 0
    
    print("Online Store")
    print(".......................................................")
    print("Product(s)\tPrice")
    
    for item, price in items.items():
        print(f"{item}\t{price}")
        total_price += price
    
    for combo, items_in_combo in combos.items():
        combo_price = sum(items[item] for item in items_in_combo)
        
        if len(items_in_combo) == 2:
            combo_price *= 0.9
        elif len(items_in_combo) == 3:
            combo_price *= 0.75
        
        print(f"{combo}\t{combo_price}")
        total_price += combo_price
    
    print(".......................................................")
    print(f"Total Price:\t{total_price}")
    print(".......................................................")
    print("For Delivery Contact: 987646678899.")

calculate_price()