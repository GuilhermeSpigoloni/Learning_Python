# Uma lista pode conter 0 ou mais elementos
# Imagine uma Lista como Um apartamento indo de 0-17 Andares sendo o 0 o Terreo e o 17 a cobertura.
# Precisa nomealo como Por exemplo P.
# Para criar em Python é: L=[]

# Lista = []
# print(type(Lista)) # --> Cria uma lista, mas com 0 elementos

# Lista com mais elementos
# P = [50, 1, 5, 3, 4]
# print(P[0])

# P = [50, 1, 5, 3, 4]
# P[0] = 0
# print(P[0])

# Calculo de média 

# notas = [6, 7, 5, 8, 9]
# soma = 0
# x = 0


# Calculo média

# notas = [5, 6, 7, 8, 9] 
# soma = sum(notas)
# print(soma)
# media = soma/len(notas)
# print(media)

# x = 0
# soma = 0

# while x < 5:
#     soma += notas[x]
#     x += 1

# print(f"Média: {soma/x: 5.2f}")

# notas = [0,0,0,0,0]
# soma = 0
# x = 0
# while x < len(notas):
#     notas[x] = float(input(f"Nota {x}: "))
#     soma += notas[x]
#     x += 1


# x = 0
# while x < len(notas):
#     print(f"Nota {x}: {notas[x]:.2f}")
#     x += 1

# print(f"Média: {soma/len(notas)}")


# notas = [0,0,0,0,0,0,0]
# soma = 0
# x = 0
# while x < len(notas):
#     notas[x] = float(input(f"{x+1}ª Nota: "))
#     soma += notas[x]
#     x += 1


# x = 0
# while x < len(notas):
#     print(f"{x+1}ª Nota: {notas[x]:.2f}")
#     x += 1

# print(f"Média: {soma/len(notas):.2f}")


notas = []
quantidade = int(input("Número de notas que serão inseridas: "))
x = 0
soma = 0

while x != quantidade:
    nota = float(input(f"Nota: {x+1}* Bim: "))
    notas.append(nota)
    x += 1

soma = sum(notas)
media = soma/len(notas)
print(f"Sua média é: {media:.2f}")



# Maneira errada de copiar uma lista --> V = l
# l = [1,2,3,4,5]
# v = l
# print(l)
# print(v)

# v[0] = 6
# print(l)
# print(v)

# # Como fazer então
# V = l[:]
# V[0] = 0

# print(l)
# print(v)
# print(V)