print("=====CONVERSION DE MINUTES EN HEURES ET MINUTES=====")
#Saisie du nombre de minutes
minutes = int(input("Entrez le nombre de minutes s'il vous plait:"))

#calcul du nombre d'heures et du reste pour les minutes
nbre_dhres = minutes // 60
reste = minutes % 60

#affichage du nombre de minutes
print("le nombre de minutes est:", minutes)

#affichage du nombre d'heures
print("le nombre d'heures est:", nbre_dhres)

#affichage du nombre de minutes apres la conversion
print("le nombre de minutes est:", reste)

