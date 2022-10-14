"""
Programme fait par Ismael Girard
Groupe: 023
Description: Programme qui permet de deviner un nombre au hasard choisi par l'ordinateur entre 0 et 100.
"""

import random

nombre_choisi = random.randint(0, 100)

print("Je suis un nombre entre 0 et 100... Je suis caché... À toi de me trouver...")

nb_essais = 1

boucle = True
while boucle:
    essai = int(input("Entrez votre essai: "))
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
            nombre_choisi = random.randint(0, 100)
            boucle = True
            nb_essais = 1
        elif nouveau_jeu == "non":
            print("À la revoyure !")
            boucle = False
        else:
            print("Ok.")
            boucle = False
