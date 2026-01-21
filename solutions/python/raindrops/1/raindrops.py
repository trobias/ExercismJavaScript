def convert(number):
    lista = ""
    if number % 3 == 0:
        lista = lista + "Pling"
    if number % 5 == 0:
        lista = lista + "Plang"
    if number % 7 == 0:
        lista = lista + "Plong"
    return lista or str(number)
