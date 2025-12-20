print("=====GESTION DE PANIER=====")
#saisie du nom du produit
produit = input ("Entrez le nom d'un produit:")

#affichage du produit saisi
print ("Vous avez saisi", produit, "comme produit.")

#saisie de la quantité
quantite = int (input("Entrez la quantité du produit:"))

#affichage de la quantité de produit
print ("Vous entrez", quantite," ",produit)

#saisie du prix unitaire
prix_unitaire = float (input("Quel est le prix unitaire du produit?"))

#affichage du prix unitaire
print("Le prix unitaire du produit est :", prix_unitaire)

#calcul du total TTC (prix x quantite)
total = prix_unitaire * quantite

#demande et verification Budget par rapport au total
budget = float(input("Quel est votre budget?"))

if total > budget:
    print("vous n’êtes pas en mesure de payer ce que vous voulez acheter")
elif total < budget:
    print("Vous pouvez faire cet achat de",total, "il te restera", budget-total)
else:
    print("vous avez l’équivalent de ce que vous achetez", "il te reste", budget-total)
