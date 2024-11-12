class ContaBancaria():
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
        
    
    def set_saldo(self, saldo):
        if isinstance(saldo ,float) and saldo >= 0:
            self.__saldo = saldo
        else:
            print("Seu saldo nunca pode ser negativo!")

saldo_inicial = 1000
conta_bancaria = ContaBancaria(saldo_inicial)

resposta = True
while resposta != 'nao' or escolha != '3':

    
    print(f"---Seja Bem Vindo!---\n- Seu saldo atual: R${conta_bancaria.get_saldo():.2f}\n1- Depósito\n2- Saque\n3- Sair")
    escolha = input("O que será hoje: ")

    if escolha == '1':
        deposito = float(input("Valor a ser depositado: R$"))
        if deposito < 0:
             print("Depósito inválido!")
        else:
            saldo_atualizado = conta_bancaria.get_saldo() + deposito
            conta_bancaria.set_saldo(saldo_atualizado)
            print(f"Saldo atual: R${conta_bancaria.get_saldo():.2f}")

    elif escolha == '2':
            saque = float(input("Valor a ser sacado: R$"))
            if saque > conta_bancaria.get_saldo():
                print(f"Você está tentando sacar mais dinheiro do que você possui! Calma lá!")
            else: 
                saldo_atualizado = conta_bancaria.get_saldo() - saque
                conta_bancaria.set_saldo(saldo_atualizado)
                print(f"Saldo atual: R${conta_bancaria.get_saldo():.2f}")


    elif escolha == '3':
            print("Saindo...")

    else:
            print("Escolha um opção válida!")
        

    if escolha == '3':
         break

    resposta = input("Deseja realizar outra ação(s/n): ").strip() .lower()
    if resposta == 'n':
        break