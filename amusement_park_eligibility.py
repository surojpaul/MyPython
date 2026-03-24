while True: 
  import datetime
  birth_year = int(input("Enter your birth year"))
  current_year = datetime.date.today().year
  calculate_year = current_year - birth_year
  if 12 <= calculate_year <= 17:
    print("You're eligible to ride Mega-Coaster")
  elif calculate_year < 12 :
    print("You're eligible to ride Junior Carousel")
  else:
    print("You can only walk")