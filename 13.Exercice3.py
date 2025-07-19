nom_fichier = input("Entrez le nom du fichier à ouvrir : ")

try:
    with open(nom_fichier, "r") as f:
        contenu = f.read()
        print(f"Contenu du fichier '{nom_fichier}' :\n{contenu}")
except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")