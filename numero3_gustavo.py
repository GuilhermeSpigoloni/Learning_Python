import math
import os
import platform

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

produtos = {
    'maçã': {'codigo': 123456, 'preco': 1.50},
    'banana': {'codigo': 234561, 'preco': 1.20},
    'laranja': {'codigo': 3456123, 'preco': 2.00},
    'uva': {'codigo': 456123, 'preco': 3.00},
    'manga': {'codigo': 561234, 'preco': 2.50},
}

# Exibe a lista de produtos disponíveis
def exibir_produtos():
    print("Produtos disponíveis:")
    for produto, info in produtos.items():
        print(f"- {produto} (Código: {info['codigo']}, Preço: R${info['preco']:.2f})")

def calcular_valor_venda(produto, quantidade):
    preco_unitario = produtos[produto]['preco']
    valor_total = preco_unitario * quantidade
    return valor_total

def entrada_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def escolher_produto():
    while True:
        exibir_produtos()
        produto = input("Escolha um produto (ou 'sair' para encerrar): ").strip().lower()
        if produto == 'sair':
            return None, None
        if produto in produtos:
            quantidade = entrada_float("Digite a quantidade comprada: ")
            return produto, quantidade
        else:
            print("Produto inválido. Tente novamente.")

def menu():
    while True:
        clear_console()
        print("Bem-vindo ao sistema de vendas!")
        
        produto, quantidade = escolher_produto()
        if produto is None:
            print("Saindo...")
            break

        valor_total = calcular_valor_venda(produto, quantidade)
        codigo_produto = produtos[produto]['codigo']

        # Exibe os dados da venda
        print("\n--- Detalhes da Venda ---")
        print(f"Código do Produto: {codigo_produto}")
        print(f"Nome do Produto: {produto.capitalize()}")
        print(f"Quantidade Comprada: {quantidade}")
        print(f"Preço Unitário: R${produtos[produto]['preco']:.2f}")
        print(f"Valor Total: R${valor_total:.2f}")
        print("-------------------------")

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja realizar outra venda? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saindo...")
            break

if __name__ == "_main_":
    menu()