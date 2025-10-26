import math

def score(x, y):
    distancia = math.sqrt(x**2 + y**2)
    if distancia <= 1:
        return 10
    elif 1 <= distancia <= 5:
        return 5
    elif 5 <= distancia <= 10:
        return 1
    elif distancia > 10:
        return 0