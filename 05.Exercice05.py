plat = input("Type de plat (viande, poisson, végétarien) : ").lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant, à point, bien cuit) : ").lower()
    print(f"Vous avez choisi de la viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron, beurre) : ").lower()
    print(f"Vous avez choisi du poisson sauce {sauce}.")
elif plat == "végétarien":
    choix = input("Souhaitez-vous une salade ou des pâtes ? (salade/pates) : ").lower()
    print(f"Vous avez choisi {choix}.")
else:
    print("Choix invalide.")