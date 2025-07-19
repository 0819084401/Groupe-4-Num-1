phrase = input("Entrez une phrase : ")
mots = phrase.split()

mots_sur_deux = mots[::2] # Prend un mot sur deux en commençant par le premier

print(f"Mots un sur deux : {mots_sur_deux}")