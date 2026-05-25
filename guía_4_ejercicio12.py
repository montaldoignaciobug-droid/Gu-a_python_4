#12. Suma de números hasta ingresar 0
#Enunciado: Simula entradas en una lista y usa while para sumar valores hasta encontrar un 0.
#Además, cuenta cuántos valores positivos y negativos hubo antes del cero.

print("\n===========================================================\n")

lista = [5, 5, - 1, 0, 7]
posicion = 0

nums_positivos = 0
nums_negativos = 0
suma_valores = 0

while posicion < len(lista) and lista[posicion] != 0:
    if lista[posicion] > 0:
        nums_positivos += 1

    elif lista[posicion] < 0:
        nums_negativos += 1

    suma_valores += lista[posicion]
    posicion += 1

print(f"Suma: {suma_valores}")
print(f"Numeros negativos: {nums_negativos}")
print(f"Numeros positivos: {nums_positivos}")

print("\n===========================================================\n")
