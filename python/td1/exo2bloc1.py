print("=====GÉNÉRATION DE MOT DE PASSE=====")
#saisie et affichage du prenom, de l'age et du symbole
prenom = input ("Saisissez votre Prénom SVP: ")
print ("Votre prénom est :", prenom)

age = int(input("Saisissez votre âge :"))
print("Votre âge est: ", age)

symbole = input("Saisissez un caractère special:")
print ("Le symbole est:", symbole)

#initialisation de la variable motdepasse
#conversion de int en str pour la concatenation puisque les variables doivent être de même type str(age)
motdepasse = prenom + str(age) + symbole

#Le mot de passe généré
#affichage du message
print("Le mot de passe généré est: ", motdepasse)