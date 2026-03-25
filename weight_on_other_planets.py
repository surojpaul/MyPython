planet_name_list = []  
user_weight = []
planet_name = 0 
user_individual_planet_weight = 0
while True:
    user_input = input("Enter your respective earth weight in kg or done: ")
    if user_input.lower() == "done":
        print("Thanks for your time.")
        break
    if user_input == 0:
        print(f"In {user_individual_planet_weight} your weight is 0")
        break
    user_earth_weight = float(user_input)
    planet_name = input("Enter the name of your planet: ")
    if planet_name.lower() == "mercury":
        user_individual_planet_weight = user_earth_weight * 0.38
    elif planet_name.lower() == "venus":
        user_individual_planet_weight = user_earth_weight * 0.9
    elif planet_name.lower() == "mars":
        user_individual_planet_weight = user_earth_weight * 0.38
    elif planet_name.lower() == "jupiter":
        user_individual_planet_weight = user_earth_weight * 2.53
    elif planet_name.lower() == "saturn":
        user_individual_planet_weight = user_earth_weight * 1.07
    else:
        print("Error: Planet not found in our charts. Please check your spelling.")
        continue
    print(f"Your weight on {planet_name} is {user_individual_planet_weight}kg")
    planet_name_list.append(planet_name)
    user_weight.append(user_individual_planet_weight)


    

