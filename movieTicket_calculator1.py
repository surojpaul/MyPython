while True:
   user_input = input("Enter your age ") 
   if user_input == "q":
      print("Thank You for your patience. Have a good day.")
      break
   try:
      age = int(user_input)
      if age <= 12:
         print("Your ticket costs $5")
      elif 12 < age <= 60:
         print("Your ticket costs $10")
      else:
         print("Your ticket costs $7")
   except:
       print("Please enter a valid number or to exit press q.")

