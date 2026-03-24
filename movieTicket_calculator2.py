group_ages = []
print("---- Build your Group (Type 0 when done) ----")
while True:
    age = int(input("Enter an age: "))
    if age == 0:
        break
    group_ages.append(age)
total_price = 0
has_adult = False
for age in group_ages:
     if 18 <= age <= 60:
        has_adult = True
     if age < 18: price = 5
     elif 18 <= age <= 60: price = 15
     else: price = 10
     total_price += price
     print(f"Age {age} : Ticket cost is ${price}")
print("-" * 10)
if not has_adult and len(group_ages) >= 0:
     print("This group can't enter without an adult.")
else:
     print(f"Group approved! Total Price: ${total_price}")
    