#6. Clasificación de edades
#Enunciado: Dada una lista de edades, recórrela con for y clasifica cada persona como niño,
#adolescente, adulto o adulto mayor.

print("\n===========================================================\n")

lista = [18, 14, 8, 51, 17, 99]

for edad in lista:
    if edad < 15:
        print(f"{edad} años: Es un niño.")
    
    elif edad >= 15 and edad < 18:
        print(f"{edad} años: Es un adolescente.")

    elif edad >= 18 and edad < 60:
        print(f"{edad} años: Es un adulto.")
    
    else:
        print(f"{edad} años: Es un adulto mayor.")

print("\n===========================================================\n")
