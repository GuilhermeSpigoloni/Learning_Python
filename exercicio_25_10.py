
#Exercicio 06 
#01

# class Pessoa():
#             def __init__(self, apelido,sobrenome ,idade ,cidade ):
#                 self.apelido = apelido
#                 self.sobrenome = sobrenome
#                 self.idade = idade
#                 self.cidade = cidade

#             def saida(self):
#                 print(f'---Essas são suas informações:--- \nNome: {self.apelido} {self.sobrenome}\nIdade: {self.idade}\nCidade: {self.cidade}')
    
# pessoa1 = Pessoa(input("Nome: "),input("Sobrenome:"),input("Idade: "),input("Cidade: "))
# pessoa2 = Pessoa(input("Nome: "),input("Sobrenome:"),input("Idade: "),input("Cidade: "))
# pessoa3 = Pessoa(input("Nome: "),input("Sobrenome:"),input("Idade: "),input("Cidade: "))

# pessoa1.saida()
# pessoa2.saida()
# pessoa3.saida()


###Lista 03 - Prática

#01
# class Carro():
#        def __init__(self):
#               self.marca = 'Lexus'
#               self.ano = 2025
#               self.cor = 'Prata'
#               self.modelo = 'RX SUV'
              
#        def saida(self):
#             return f"------Carro------\nMarca:{self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\n-----------------"


# carro = Carro()
# print(f"{carro.saida()}")



#02
# class Personagem:
#        def __init__(self,classe,arma,vida,mana,forca,velocidade,nome):
#               self.nome = nome
#               self.classe = classe
#               self.arma = arma
#               self.vida = vida
#               self.mana = mana
#               self.forca = forca
#               self.velocidade = velocidade
        
#        def saida(self):
#               print (f"-------Your Profile-------\nNick: {self.nome}\nClasse: {self.classe}\nArma: {self.arma}\nVida: {self.vida}HP\nMana: {self.mana}\nForça: {self.forca}\nVelocidade: {self.velocidade}\n--------------------")
       
# atributos = Personagem(input("Nickname: "),input("Classe: "), input("Arma: "), input("Vida: "), input("Mana: "), input("Força: "), input("Velocidade: "))
# atributos.saida()





#3
class ContaBancaria:
       def __init__(self,dono,adicional):
              self.dono = dono
              self.saldo = 1000
              self.adicional = adicional


       def saida(self):
              print(f"---DADOS BANCÁRIOS---\nCliente: {self.dono}\nSaldo: {self.saldo+self.adicional}\n---------------------")

adicional = ContaBancaria(input("Nome: "),(int(input("Valor do depósito: R$"))))
adicional.saida()