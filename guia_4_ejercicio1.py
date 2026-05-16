#1. Clasificación de números del 1 al 20
#Enunciado: Recorre los números del 1 al 20 con un ciclo for. Para cada número indica si es par,
#impar o si además es múltiplo de 5. Usa operadores condicionales y una estructura if / elif / else.

print("\n===========================================================\n")

for i in range(1, 21):
    if i % 2 == 0 and i % 5 == 0:
        print(f"{i}: es un número par y múltiplo de 5.\n")

    elif i % 2 == 0 and i % 5 != 0:
        print(f"{i}: es un número par pero no es múltiplo de 5.\n")

    elif i % 2 != 0 and i % 5 == 0:
        print(f"{i} es impar y múltiplo de 5.\n")

    else:
        print(f"{i} es un número impar pero no múltiplo de 5.\n")

print("\n===========================================================\n")