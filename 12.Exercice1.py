noms_utilisateurs = []
nom = ""

print("Entrez les noms d'utilisateurs. Tapez 'stop' pour terminer.")
while nom != "stop":
    nom = input("Nom de l'utilisateur : ").lower()
    if nom != "stop":
        noms_utilisateurs.append(nom)

nom_fichier = "utilisateurs.txt"
with open(nom_fichier, "w") as f:
    for user in noms_utilisateurs:
        f.write(user + '\n')

print(f"Les utilisateurs ont été enregistrés dans '{nom_fichier}'.")