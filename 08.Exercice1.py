livres = [
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "année": 1954},
    {"titre": "Sapiens", "auteur": "Yuval Noah Harari", "année": 2014},
    {"titre": "Factfulness", "auteur": "Hans Rosling", "année": 2018},
    {"titre": "1984", "auteur": "George Orwell", "année": 1949}
]

print("Livres publiés après 2010 :")
for livre in livres:
    if livre["année"] > 2010:
        print(f"- {livre['titre']} par {livre['auteur']} ({livre['année']})")