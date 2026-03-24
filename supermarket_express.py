item_numbers = []
print("-----Price calculator of your items (max. 10 and type 0 to exit-----)")
while True:
    item = float(input("Enter the price of item "))
    if item == 0:
     print("Thanks for coming. Have a good day!")
     break
    item_numbers.append(item)
    if len(item_numbers) == 10:
     print("you've reached your item limit.")
     break
total = 0
for item in item_numbers:
    total += item
print("-" * 20)
print(f"TOTAL BILL: ${total}")

    
    