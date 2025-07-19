import datetime

activite = input("Entrez une activité à ajouter au journal : ")
nom_fichier = "journal_activites.txt"

# Obtenir la date et l'heure actuelles
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(nom_fichier, "a") as f:
    f.write(f"[{timestamp}] : {activite}\n")

print(f"L'activité a été ajoutée au journal '{nom_fichier}'.")