distancia = float(input("Distância que deseja percorrer(km): "))
if distancia <= 200:
    valor = distancia * 0.50
    print(f"Valor da passagem: R${valor:.2f}")
else: 
    valor = distancia * 0.45
    print(f"Valor da passagem: R${valor:.2f}")