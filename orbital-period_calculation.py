import math
def calculate_orbital_period_seconds(semi_major_axis, individual_central_object_mass):
    G = 6.67e-11
    orbital_period_seconds = 2 * math.pi * math.sqrt((semi_major_axis**3) / (G * individual_central_object_mass))
    return orbital_period_seconds
def format_time(orbital_period_seconds):
    minutes, seconds = divmod(orbital_period_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds"
print("----Orbital Period Calculator for Planets and Stars----")
semi_major_axis_list = []
central_object_mass_list = []
central_object_name_list = []
celestrial_body_name_list = []
while True:
    individual_celestrial_body_name = input("Enter the name of the celestrial body: ")
    if individual_celestrial_body_name == "done":
        print("Thanks for your time")
        break
    individual_central_object_name = input("Enter the name of the central object: ")
    if individual_central_object_name == "done":
        print("Thanks for your time")
        break
    user_input_semi_major_axis = input("Enter the semi-major axis of the orbit (in meters): ")
    try:
        semi_major_axis = float(user_input_semi_major_axis)
    except ValueError:
        print("Error!! Please enter a numeric value for semi-major axis.")
        continue    
    if semi_major_axis <= 0:
        print(f"Orbital period of the {individual_celestrial_body_name} is undefined")
        break
    user_input_central_object_mass = input("Enter the mass of the central object (in kg): ")
    try:
        individual_central_object_mass = float(user_input_central_object_mass)
    except ValueError:
        print("Error!! Please enter a numeric value for central object mass.")
        continue    
    if individual_central_object_mass <= 0:
        print(f"Orbital period of the {individual_celestrial_body_name} is undefined")
        break
    orbital_period_seconds = calculate_orbital_period_seconds(semi_major_axis, individual_central_object_mass)
    formatted_time = format_time(orbital_period_seconds)
    print(f"Orbital period of the {individual_celestrial_body_name} is {formatted_time}")
    celestrial_body_name_list.append(individual_celestrial_body_name)
    semi_major_axis_list.append(semi_major_axis)
    central_object_mass_list.append(individual_central_object_mass)
    central_object_name_list.append(individual_central_object_name)