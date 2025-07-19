etudiants_notes = [
    ("Alice", 18),
    ("Bob", 12),
    ("Charlie", 16),
    ("David", 9),
    ("Eve", 15)
]

print("Étudiants avec une note >= 15 :")
for nom, note in etudiants_notes:
    if note >= 15:
        print(f"- {nom} : {note}")