G = 6.67e-11
planet_mass = []
planet_radius = []
planet_name = []
while True:
    individual_planet_name = input("Enter the name of the planet: ")
    if individual_planet_name == "done":
        print("Thanks for your time")
        break
    user_input_mass = input("Enter the mass of the planet (in kg): ")
    individual_planet_mass = float(user_input_mass) 
    if individual_planet_mass == 0:
        print(f"Escape velocity of the {individual_planet_name}  is 0")
        break
    user_input_radius = input("Enter the radius of the planet (in meters): ")
    individual_planet_radius = float(user_input_radius)
    if individual_planet_radius == 0:
        print(f"Escape velocity of the {individual_planet_name} is infinite")
        break
    import math
    escape_velocity = math.sqrt((2*G*individual_planet_mass)/individual_planet_radius)
    print(f"Escape velocity of the {individual_planet_name} is {escape_velocity/1000:.2f} Km/s")
    if escape_velocity > 300000:
        print("Watch out!! It's a freaking BLACKHOLE!!!")
    planet_name.append(individual_planet_name)
    planet_mass.append(individual_planet_mass)
    planet_radius.append(individual_planet_radius)

