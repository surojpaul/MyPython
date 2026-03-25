shopping_list = []
running_total = 0
original_price = 0
total_tax = 0
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
        tax = discounted_price * 0.1
    elif 500 <= user_item_price < 1000:
        discounted_price = user_item_price - user_item_price * 0.1 
        tax = discounted_price * 0.2
    elif 1000 <= user_item_price < 5000:
        discounted_price = user_item_price - user_item_price * 0.2
        tax = discounted_price * 0.3
    else:
        discounted_price = user_item_price - user_item_price * 0.3
        tax = discounted_price * 0.5
    running_total += discounted_price
    total_tax += tax
print("*" * 30)
print(f"ITEMS IN CART: {shopping_list}")
print(f"TOTAL AMOUNT: ${running_total}")
print(f"TAX AMOUNT: ${total_tax}")
print(f"GRAND TOTAL: ${running_total + total_tax}")
print(f"TOTAL SAVINGS: ${original_price - running_total}")
exit()

     
