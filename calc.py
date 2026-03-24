code = input("Enter security code: ")

if code == "1234":
 print("Access Granted!")
 try:
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print(f"The total is: {num1 + num2}")
 except ValueError:
  print("Error: You must type a NUMBER, not words!")
else: 
 print("Wrong code! No math for you.")