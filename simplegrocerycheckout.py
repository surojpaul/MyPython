shopping_cart = []
running_total = 0
while True:
    user_input_name = input("Enter the name of the item ")
    if user_input_name == "done":
        print("Thanks for coming. Have a good day!")
        break
    user_input_price = input("Enter the price of the item ")
    item_price = float(user_input_price)
    try:
        item_price = float(user_input_price)
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        continue
    running_total += item_price
    if running_total > 100:
        print("Warning! You've crossed $100 mark!")
    shopping_cart.append(user_input_name)
print("*" * 20)
print(f"ITEMS IN CART: {shopping_cart}")
print(f"TOTAL BILL: ${running_total}")
