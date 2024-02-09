# def math_formula():
#     return 5


# def science_formula():
#     return 6

def gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^−1 s^−2
    force = G * (mass1 * mass2) / (distance ** 2)
    return force
