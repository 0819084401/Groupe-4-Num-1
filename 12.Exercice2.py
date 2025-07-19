nombre = int(input("Entrez un nombre pour générer sa table de multiplication : "))
nom_fichier = f"table_de_{nombre}.txt"

with open(nom_fichier, "w") as f:
    f.write(f"--- Table de multiplication de {nombre} ---\n")
    for i in range(1, 13):
        f.write(f"{nombre} x {i} = {nombre * i}\n")

print(f"La table de multiplication a été enregistrée dans '{nom_fichier}'.")