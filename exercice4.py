
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    #annees= secondes//le nombre de secondes dans une année
	#secondesrestantes=secondes%(365*24*3600)
    annees = secondes//(365*24*3600)
    secondes %= 365*24*3600

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    #semainesRestantes= secondesRestantes% le nombre de secondes dans une semaine
    semaines = secondes//(24*3600*7)
    secondes %= 7*24*3600

    # TODO: Assigner à la variable "jours" le nombre de jours restants
	 #joursRestants= semainesRestantes% le nombre de jours dans une semaine
    jours = secondes//(24*60*60)
    secondes %= 24*60*60

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
	 #heuresRestantes= joursRestants% le nombre de secondes dans une semaine
    heures = secondes//3600
    secondes %= 60*60

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
	 #minutesRestantes= heuresRestantes% le nombre de secondes dans une semaine
    minutes = secondes//60


    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
	 #secondesRestantesAuFinal= minutesRestantes% le nombre de secondes dans une semaine
    secondes %= 60

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures,minutes,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    decomposer(secondes)
