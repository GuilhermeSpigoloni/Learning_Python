def calcular_notas():
    resposta = "S"

    while resposta.upper() == "S":
        nome = input("Escreva seu nome completo: ")
        i = input("Qual matéria deseja consultar?\n 1-Matemática\n 2-Português\n 3-Ciências\n 4-Todas\n")

        if i == "1":
            n1 = float(input("Digite suas notas de Matemática\nPrimeiro Bimestre: "))
            n2 = float(input("Segundo Bimestre: "))
            n3 = float(input("Terceiro Bimestre: "))
            n4 = float(input("Quarto Bimestre: "))
            resultado = n1 + n2 + n3 + n4
            mediaM = resultado / 4
            print(f"Sua média é: {mediaM:.2f}\n")
            if mediaM >= 7:
                print(f"Aqui está seu resultado em matemática {nome}\nSua média nesta disciplina foi: {mediaM:.2f}\nParabéns, você foi aprovado!!")
            elif 5 <= mediaM < 6.9:
                print(f"Sua média foi: {mediaM:.2f}\nVocê está de recuperação!")
            else:
                print(f"Sua média foi: {mediaM:.2f}\nVocê foi reprovado!")

        elif i == "2":
            n1 = float(input("Digite suas notas de Português\nPrimeiro Bimestre: "))
            n2 = float(input("Segundo Bimestre: "))
            n3 = float(input("Terceiro Bimestre: "))
            n4 = float(input("Quarto Bimestre: "))
            resultado = n1 + n2 + n3 + n4
            mediaP = resultado / 4
            print(f"Sua média é: {mediaP:.2f}\n")
            if mediaP >= 7:
                print(f"Aqui está seu resultado em português {nome}\nSua média nesta disciplina foi: {mediaP:.2f}\nParabéns, você foi aprovado!!")
            elif 5 <= mediaP < 6.9:
                print(f"Sua média foi: {mediaP:.2f}\nVocê está de recuperação!")
            else:
                print(f"Sua média foi: {mediaP:.2f}\nVocê foi reprovado!")

        elif i == "3":
            n1 = float(input("Digite suas notas de Ciências\nPrimeiro Bimestre: "))
            n2 = float(input("Segundo Bimestre: "))
            n3 = float(input("Terceiro Bimestre: "))
            n4 = float(input("Quarto Bimestre: "))
            resultado = n1 + n2 + n3 + n4
            mediaC = resultado / 4
            print(f"Sua média é: {mediaC:.2f}\n")
            if mediaC >= 7:
                print(f"Aqui está seu resultado em ciências {nome}\nSua média nesta disciplina foi: {mediaC:.2f}\nParabéns, você foi aprovado!!")
            elif 5 <= mediaC < 6.9:
                print(f"Sua média foi: {mediaC:.2f}\nVocê está de recuperação!")
            else:
                print(f"Sua média foi: {mediaC:.2f}\nVocê foi reprovado!")

        elif i == "4":
            # Notas de Matemática
            n1M = float(input("Digite suas notas de Matemática\nPrimeiro Bimestre: "))
            n2M = float(input("Segundo Bimestre: "))
            n3M = float(input("Terceiro Bimestre: "))
            n4M = float(input("Quarto Bimestre: "))
            mediaM = (n1M + n2M + n3M + n4M) / 4

            # Notas de Português
            n1P = float(input("Digite suas notas de Português\nPrimeiro Bimestre: "))
            n2P = float(input("Segundo Bimestre: "))
            n3P = float(input("Terceiro Bimestre: "))
            n4P = float(input("Quarto Bimestre: "))
            mediaP = (n1P + n2P + n3P + n4P) / 4

            # Notas de Ciências
            n1C = float(input("Digite suas notas de Ciências\nPrimeiro Bimestre: "))
            n2C = float(input("Segundo Bimestre: "))
            n3C = float(input("Terceiro Bimestre: "))
            n4C = float(input("Quarto Bimestre: "))
            mediaC = (n1C + n2C + n3C + n4C) / 4

            print(f"Aqui estão seus resultados, {nome}\n")

            # Resultado de Matemática
            print(f"Sua média em Matemática foi: {mediaM:.2f}")
            if mediaM >= 7:
                print("Parabéns, você foi aprovado!")
            elif 5 <= mediaM <= 6.9:
                print("Você está de recuperação")
            else:
                print("Você foi reprovado")

            # Resultado de Português
            print(f"Sua média em Português foi: {mediaP:.2f}")
            if mediaP >= 7:
                print("Parabéns, você foi aprovado!")
            elif 5 <= mediaP <= 6.9:
                print("Você está de recuperação")
            else:
                print("Você foi reprovado")

            # Resultado de Ciências
            print(f"Sua média em Ciências foi: {mediaC:.2f}")
            if mediaC >= 7:
                print("Parabéns, você foi aprovado!")
            elif 5 <= mediaC <= 6.9:
                print("Você está de recuperação")
            else:
                print("Você foi reprovado")
        else:
            print("Disciplina inválida!")

        resposta = input("\n\nDeseja calcular para outro aluno? (S/N): ")

calcular_notas()