#3. Conteo de positivos, negativos y ceros
#Enunciado: Dada una lista de enteros, recórrela con for y cuenta cuántos números son positivos,
#cuántos negativos y cuántos ceros hay.

print("\n===========================================================\n")

lista = [0, 2, 3, 4, -1, -2]
print(lista)

contador_positivos = 0
contador_negativo = 0
contador_ceros = 0

for entero in lista:
    if entero > 0:
        contador_positivos += 1

    elif entero < 0:
        contador_negativo += 1

    else:
        contador_ceros += 1

print(f"\nCantidad de ceros: {contador_ceros}")
print(f"Cantidad de negativos: {contador_negativo}")
print(f"Cantidad de positivos: {contador_positivos}")

print("\n===========================================================\n")
