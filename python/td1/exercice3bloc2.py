print("=====TESTEUR DE CONDITIONS MULTIPLES=====")
#saisie de l'âge
age = int(input("Entrez votre âge:"))

#affichage de l'âge
print("Vous avez", age, "ans")

#saisie du score
score = int(input("Entrez votre score:"))

#affichage du score
print("Votre score est :", score)

#vérification de conditions
if age>=18 and score >= 50 :
    print("Accès autorisé")
elif age < 18 and score < 50:
    print ("Accès refusé")

