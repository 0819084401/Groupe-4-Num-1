phrase = input("Entrez un titre ou une phrase : ")
mots = phrase.split()
acronyme = ""

for mot in mots:
    if mot: # S'assurer que le mot n'est pas vide
        acronyme += mot[0].upper()

print(f"Acronyme : {acronyme}")