import math
def calculate_orbital_velocity(central_object_mass, semi_major_axis, eccentricity):
    G = 6.67430e-11
    # Calculate the distance at the point of interest (e.g., periapsis or apoapsis)
    radius_peri = semi_major_axis * (1 - eccentricity)  # For periapsis
    radius_apo = semi_major_axis * (1 + eccentricity)  # For apoapsis
    velocity_peri = math.sqrt(G * central_object_mass * (2/radius_peri - 1/semi_major_axis))
    velocity_apo = math.sqrt(G * central_object_mass * (2/radius_apo - 1/semi_major_axis))
    return velocity_peri, velocity_apo
object_name_list = []
central_object_name_list = []
central_object_mass_list = []
semi_major_axis_list = []
eccentricity_list = []
while True:
    user_input_name = input("Enter the object name, central object name (or 'done' to finish): ")
    if user_input_name.lower() == 'done':
        break
    user_input_calculation = input("Enter the central object mass (kg), semi-major axis (m), and eccentricity (0-1) separated by commas: ")
    try:
        object_name, central_object_name = user_input_name.split(",")
        object_name_list.append(object_name)
        central_object_name_list.append(central_object_name)
    except ValueError:
        print("Invalid name format. Please enter exactly two names seperated by a comma.")
    try:
        central_object_mass, semi_major_axis, eccentricity = map(float, user_input_calculation.split(','))
        if not (0 <= eccentricity < 1):
            print("Eccentricity must be between 0 and 1. Please try again.")
            continue
        central_object_mass_list.append(central_object_mass)
        semi_major_axis_list.append(semi_major_axis)
        eccentricity_list.append(eccentricity)
    except ValueError:
        print("Invalid input. Please enter three numbers separated by commas.")
for object_name, central_object_name, central_object_mass, semi_major_axis, eccentricity in zip(object_name_list, central_object_name_list, central_object_mass_list, semi_major_axis_list, eccentricity_list):
    velocity_peri, velocity_apo = calculate_orbital_velocity(central_object_mass, semi_major_axis, eccentricity)
    print(f"----Results for {object_name} orbiting {central_object_name}----")
    print(f"Central object mass: {central_object_mass} kg, Semi-Major Axis: {semi_major_axis} m, Eccentricity: {eccentricity}")
    print(f"Orbital Velocity at Periapsis: {velocity_peri/1000:.2f} Km/s")
    print(f"Orbital Velocity at Apoapsis: {velocity_apo/1000:.2f} Km/s")

    