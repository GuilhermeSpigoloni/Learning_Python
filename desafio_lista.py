num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = num1[::-2]
impares = num2[::2]
soma_pares = sum(pares)
soma_impares = sum(impares)

print(f"LISTA: {lista[::-1]}")
print(f"Numeros impares: {impares}")
print(f"Numeros pares: {pares}")

print(f"Soma numeros pares: {soma_pares}")
print(f"Soma impares: {soma_impares}")
multiplicacao = soma_pares * soma_impares
print(f"Multimplicacao dos resultados: {multiplicacao}")