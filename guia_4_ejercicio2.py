#2. Promedio de notas y estado del estudiante
#Enunciado: Guarda 5 notas en una lista. Recorre la lista con for, calcula el promedio y determina
#si el estudiante aprueba, habilita o reprueba. Considera: promedio >= 4.0 aprueba, entre 3.0 y
#3.9 habilita, menor a 3.0 reprueba.

print("\n===========================================================\n")

nota_1 = float(input("Introduzca una nota: "))
nota_2 = float(input("Introduzca otra nota: "))
nota_3 = float(input("Introduzca otra nota: "))
nota_4 = float(input("Introduzca otra nota: "))
nota_5 = float(input("Introduzca otra nota: "))

suma_notas = 0

lista = [nota_1, nota_2, nota_3, nota_4, nota_5]

for notas in lista:
    suma_notas = notas + suma_notas

promedio = suma_notas / len(lista)
print(f"Promedio: {promedio:.1f}")

if promedio >= 4.0:
     print("¡El estudiante aprueba!")
    
elif promedio >= 3.0 and promedio <= 3.9:
      print("El estudiante está habilitado.")

else:
      print("El estudiante reprueba.")


print("\n===========================================================\n")
