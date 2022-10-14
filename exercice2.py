"""
Programme fait par Ismael Girard
Groupe: 023
Description: Programme qui permet de deviner un nombre au hasard entre deux bornes choisies par l'usager (c'est l'ordinateur qui choisit le nombre au hasard).
"""

import random

print("Vous devez deviner un nombre que je choisirai au hasard entre deux bornes que vous delimiterez... Bonne chance...")

nombre_usager1 = int(input("Choisissez la premiere borne: "))
nombre_usager2 = int(input("Choisissez la deuxieme borne: "))

nombre_choisi = random.randint(nombre_usager1, nombre_usager2)

nb_essais = 1

boucle = True
while boucle:
    essai = int(input("Entrez votre essai:"))
    if essai > nombre_choisi:
        print("Non. Plus petit.")
        nb_essais += 1
    elif essai < nombre_choisi:
        print("Non. Plus grand.")
        nb_essais += 1
    if essai == nombre_choisi:
        print("Tu m'as trouvé en", nb_essais, "essais...")
        nouveau_jeu = input("Voulez-vous rejouer? (oui/non)")
        if nouveau_jeu == "oui":
            nombre_usager1 = int(input("Choisissez la premiere borne: "))
            nombre_usager2 = int(input("Choisissez la deuxieme borne: "))
            nombre_choisi = random.randint(nombre_usager1, nombre_usager2)
            boucle = True
            nb_essais = 1
        elif nouveau_jeu == "non":
            print("À la revoyure !")
            boucle = False
        else:
            print("Ok.")
            boucle = False
