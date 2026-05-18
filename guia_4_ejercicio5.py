#5. Análisis de vocales y consonantes
#Enunciado: Recorre una cadena con for y cuenta cuántas vocales, consonantes y espacios tiene.
#Ignora los caracteres que no sean letras ni espacios.

print("\n===========================================================\n")

palabra = input("Ingrese una palabra o frase: ")
vocales = 0
consonantes = 0
espacios = 0


for letra in palabra.lower():
    
    if letra in "aeiou":
        vocales += 1

    elif letra == " ":
        espacios += 1

    elif letra.isalpha():
        consonantes += 1

print(f"Cantidad de vocales: {vocales}")
print(f"Cantidad de consonantes: {consonantes}")
print(f"Cantidad de espacios: {espacios}")

print("\n===========================================================\n")
