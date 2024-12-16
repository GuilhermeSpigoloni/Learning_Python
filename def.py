import math
import os
import platform

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def maiorNumero(a, b):
    return max(a, b)

def entrada_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

def escolher_operacao(opcao):
    if opcao == "1":
        return soma(
            entrada_float("Digite o primeiro número: "),
            entrada_float("Digite o segundo número: ")
        )
    elif opcao == "2":
        return subtracao(
            entrada_float("Digite o primeiro número: "),
            entrada_float("Digite o segundo número: ")
        )
    elif opcao == "3":
        return maiorNumero(
            entrada_float("Digite o primeiro número: "),
            entrada_float("Digite o segundo número: ")
        )

    else:
        print("Opção inválida!")
        return None

def menu():
    while True:
        clear_console()
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Maior número")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo...")
            break

        resultado = escolher_operacao(opcao)
        if resultado is not None:
            print(f"Resultado: {resultado}")

        continuar_calculo = input("Deseja continuar no mesmo cálculo? (s/n): ").strip().lower()
        if continuar_calculo != 's':
            print("Voltando ao menu...")

if __name__ == "__main__":
    menu()