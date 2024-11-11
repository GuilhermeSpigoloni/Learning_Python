def média_gasolina():
#calculando a média de gasolina gasta em uma viagem

    print("Vamos calcular o quanto de combustível você gastou na viagem!")

    horas = int(input("Quanto tempo durou sua viagem? (em horas) "))
    velocidade_media = int(input("Qual foi sua velocidade média durante o trajeto? (em km/h) "))
    distancia_percorrida= horas*velocidade_media

    combustivel = distancia_percorrida/12
    print(f"Você gastou uma média de {combustivel:.3f} de gasolina!")



média_gasolina()