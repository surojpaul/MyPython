while True:
       user_input = input("Enter how old are you: ")
       
       if user_input == "q":
           print("Goodbye!")
           break
       try:
         age = int(user_input) 
         if age <= 5:
            print("You're in early childhood")
         elif age <= 12:
            print("You're a school aged child")
         elif age <= 18:
            print("You're a juvenile")
         elif age <= 40:
            print("You're a young adult")
         elif age <= 65:
            print("You're a middle-aged-adult")
         else:
            print("You're a older adult")
       except ValueError:
         print("Please enter a valid number or for exit press q")
       