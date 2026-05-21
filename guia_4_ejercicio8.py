#8. Tabla de multiplicar con validación
#Enunciado: Dado un número, genera su tabla de multiplicar del 1 al 10 con un for. Si el número
#es menor o igual que 0, informa que no es válido.

print("\n===========================================================\n")

numero = int(input("Ingrese un número: "))

if numero == 0 or numero < 0:
    print("No es válido.")

else:
    for num in range(1, 11):
        multi = num * numero
        print(f"{num} x {numero} = {multi}")

print("\n===========================================================\n")
