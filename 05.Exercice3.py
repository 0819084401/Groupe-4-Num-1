# Demander une chaîne à l'utilisateur
chaine_originale = input("Entrez une chaîne de caractères : ")

# Initialiser une chaîne vide pour stocker la version inversée
chaine_inversee = ""

# Parcourir la chaîne originale à l'envers et construire la chaîne inversée
for caractere in chaine_originale:
    chaine_inversee = caractere + chaine_inversee

# Afficher la chaîne inversée
print(f"Chaîne inversée : {chaine_inversee}")