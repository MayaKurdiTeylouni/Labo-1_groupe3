def calculerEnergie(masse, vitesse):
    # TODO convertir la vitesse en metre par seconde, assigner la valeur à la variable "vitesse"
    vitesse = (vitesse * 1000) / 3600

    # TODO calculer l'energie cinetique, assigner la valeur à la variable "energieCinetique"
    energieCinetique = float(1) / 2 * masse * (vitesse ** 2)
    return energieCinetique


if __name__ == '__main__':
    masse = float(input("indiquez la masse(en kg) de la voiture: "))
    vitesse = float(input("indiquez la vitesse (en km/h) de la voiture: "))
    calculerEnergie(masse, vitesse)
print(calculerEnergie(masse, vitesse))
