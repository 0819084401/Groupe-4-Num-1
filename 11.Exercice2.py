def calculer(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Division par zéro impossible"
    else:
        return "Opération invalide"

# Exemples d'utilisation
print(f"5 + 3 = {calculer(5, 3, '+')}")
print(f"10 / 2 = {calculer(10, 2, '/')}")
print(f"7 * 4 = {calculer(7, 4, '*')}")
print(f"6 - 9 = {calculer(6, 9, '-')}")
print(f"10 / 0 = {calculer(10, 0, '/')}")
print(f"5 ^ 2 = {calculer(5, 2, '^')}")