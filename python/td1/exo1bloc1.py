print("=====CALCUL DE RÉDUCTION APRÈS POURCENTAGE=====")
#saisie du prix
prix= float(input("Entrez un prix:"))

#affichage d'un message pour le prix saisi
print("Le prix saisi est:",prix)

#saisie du pourcentage
pourcentage = int(input("Entrez le pourcentage:"))

#affichage d'un message pour le pourcentage saisi
print("Le pourcentage est:", pourcentage)

#initialisation de la variable calcul_final
calcul_final = prix - (prix * pourcentage/100)

#affichage de message pour le calcul final
print("Le calcul final est:", calcul_final)