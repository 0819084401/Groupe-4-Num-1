# Lecture des données
distance_km = float(input("Distance (km) : "))
temps_h = float(input("Temps (heures) : "))

# Calculs
vitesse_kmh = distance_km / temps_h
vitesse_ms = (distance_km * 1000) / (temps_h * 3600)

# Affichage
print(f"Vitesse moyenne : {vitesse_kmh:.2f} km/h")
print(f"Vitesse moyenne : {vitesse_ms:.2f} m/s")