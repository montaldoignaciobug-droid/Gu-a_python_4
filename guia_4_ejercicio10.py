#10. Descuentos en una lista de compras
#Enunciado: Recorre una lista de precios con for. Si un precio es mayor a 100 aplica 20% de
#descuento, si es mayor o igual a 50 aplica 10%, de lo contrario no aplica descuento.

print("\n===========================================================\n")

lista = [10, 50, 60, 100, 120, 30]

for valor in lista:
    if valor > 100:
        valor_final = valor * 0.80
        print(f"Valor final: {valor_final:.1f}")

    elif valor >= 50:                
        valor_final = valor * 0.90
        print(f"Valor final: {valor_final:.1f}")

    else:
        print(f"Valor final: {valor:.1f}")

print("\n===========================================================\n")
