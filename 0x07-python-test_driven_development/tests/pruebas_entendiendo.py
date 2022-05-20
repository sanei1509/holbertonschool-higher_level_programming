from math import pi

def circle_area(r):
    """calculo que devuelve el area de un circulo"""
    return pi*(r**2)

# Test function
"""lista de valores de radios que probamos recibir"""
radio = [2, 3, -3, 2 + 5j, True, "hola"]
mensaje = "El area de circulos with r = {radius} is {area}"

"""Damos formato al mensaje"""
for r in radio:
    A = circle_area(r)
    print(mensaje.format(radius=r, area=A))
