phrase = input("Entrez une phrase : ")
mots = phrase.split()

mots_longs_count = 0
for mot in mots:
    # Nettoyer le mot (ex: enlever ponctuation)
    mot_nettoye = ''.join(filter(str.isalpha, mot))
    if len(mot_nettoye) > 5:
        mots_longs_count += 1

print(f"Nombre de mots de plus de 5 lettres : {mots_longs_count}")