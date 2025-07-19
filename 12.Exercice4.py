entree_notes = input("Entrez une liste de notes séparées par des espaces : ")
notes = [float(x) for x in entree_notes.split()]

nom_fichier = "statistiques_notes.txt"

if notes:
    moyenne = sum(notes) / len(notes)
    with open(nom_fichier, "w") as f:
        f.write(f"Statistiques des notes :\n")
        f.write(f"Nombre de notes : {len(notes)}\n")
        f.write(f"Moyenne : {moyenne:.2f}\n")
    print(f"Les statistiques ont été enregistrées dans '{nom_fichier}'.")
else:
    print("Aucune note saisie, pas de statistiques à enregistrer.")