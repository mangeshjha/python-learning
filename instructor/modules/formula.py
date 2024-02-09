# from formula import math_formula,science_formula
# import formula

# import modules
# print(modules.math_formula())
# print(modules.science_formula())

# import modules
# print(modules.gravitational_force(1,2,3))

import modules
mass_earth = 5.972e24
mass_moon = 7.342e22

distance_earth_moon = 384.4e6

force_earth_moon = modules.gravitational_force(mass_earth, mass_moon, distance_earth_moon)

print(f"The gravitational force between Earth and Moon is {force_earth_moon:.2e} Newtons.")