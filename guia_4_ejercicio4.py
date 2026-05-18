#4. Números divisibles por 3 o por 7
#Enunciado: Muestra los números del 1 al 50 que sean divisibles por 3 o por 7, pero no por ambos
#al mismo tiempo. Usa operadores lógicos.

print("\n===========================================================\n")

for num in range(1, 51):

    if num % 3 == 0 and num % 7 != 0:
        print(num)

    elif num % 7 == 0 and num % 3 != 0:
        print(num)

print("\n===========================================================\n")