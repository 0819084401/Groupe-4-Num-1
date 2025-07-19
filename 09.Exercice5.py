phrase = input("Entrez une phrase : ")
mot_a_masquer = input("Entrez le mot à masquer : ")

# Créer la chaîne d'astérisques de la même longueur que le mot
masque = '*' * len(mot_a_masquer)

# Remplacer toutes les occurrences du mot
phrase_masquee = phrase.replace(mot_a_masquer, masque)

print(f"Phrase masquée : {phrase_masquee}")