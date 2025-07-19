phrase = input("Entrez une phrase pour l'analyse : ")
nom_fichier = "rapport_analyse_texte.txt"

nombre_mots = len(phrase.split())
nombre_caracteres = len(phrase) # Inclut les espaces et ponctuations

with open(nom_fichier, "w") as f:
    f.write("--- Rapport d'analyse de texte ---\n")
    f.write(f"Phrase analysée : \"{phrase}\"\n")
    f.write(f"Nombre de mots : {nombre_mots}\n")
    f.write(f"Nombre de caractères (espaces inclus) : {nombre_caracteres}\n")

print(f"Un rapport d'analyse a été créé dans '{nom_fichier}'.")