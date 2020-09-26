import math


def calculerNombreChiffres(nombre):
    # TODO: Déterminer le nombre de chiffres de "nombre" et mettre la valeur dans "nombreDeChiffre"

    i = 0
    while (nombre > 0):
        nombre = nombre // 10
        i += 1
    return i


if __name__ == '__main__':
    nombre = int(input('veuillez indiquer un nombre strictement postif: '))
    calculerNombreChiffres(nombre)
    print(calculerNombreChiffres(nombre))
