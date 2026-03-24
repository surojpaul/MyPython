shopping_list = []
running_total = 0
original_price = 0
while True:
    user_item_name = input("Enter the name of your item ")
    if user_item_name.lower() == "done":
        print("Thanks for coming. Have a good day!")
        break
    shopping_list.append(user_item_name)
    user_item_price = float(input("Enter the price of your item "))
    original_price += user_item_price
    if user_item_price < 500:
        discounted_price = user_item_price
    elif 500 <= user_item_price < 1000:
        discounted_price = user_item_price - user_item_price * 0.1 
    elif 1000 <= user_item_price < 5000:
        discounted_price = user_item_price - user_item_price * 0.2
    else:
        discounted_price = user_item_price - user_item_price * 0.3
    running_total += discounted_price
print("*" * 30)
print(f"ITEMS IN CART: {shopping_list}")
print(f"GRAND TOTAL: ${running_total}")
print(f"TOTAL SAVINGS: ${original_price - running_total}")

     
