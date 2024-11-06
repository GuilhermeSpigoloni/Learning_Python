#Lista 04 - Prática

# 1
# class Pessoa():
#     def __init__(self, nome):
#         self.__nome = nome

#     def get_nome(self):
#         return self.__nome



# nome = input("Nome: ")
# pessoa = Pessoa(nome)
# print(pessoa.get_nome())



# 2
# class Pessoa():
#     def __init__(self, nome):
#         self.__nome = nome

#     def get_nome(self):
#         return self.__nome
#     def set_nome(self, nome):
#          if isinstance(nome, str) and len(nome) > 0:
#              self.__nome = nome
#          else:
#              print("Nome Inválido!")


# nome = input("Nome: ")
# pessoa = Pessoa(nome)
# pessoa.set_nome(nome)
# print(pessoa.get_nome())



# 3
# class Carro():
#     def __init__(self, modelo, dono):
#         self.__modelo = modelo
#         self.__dono = dono
    
#     def get_modelo(self):
#         return self.__modelo
        
#     def set_modelo(self, modelo):
#         if isinstance(modelo, str) and len(modelo) > 0:
#             self.__modelo = modelo
#         else:
#             print("Modelo Inválido!")

#     def get_dono(self):
#         return self.__dono
    
#     def set_dono(self, dono):
#         if isinstance(dono , str) and len(dono) > 0:
#             self.__dono = dono
#         else:
#             print("Nome inválido!")


# dono = input("Proprietário do veículo: ")
# modelo = input("Modelo: ")
# carro = Carro(modelo, dono)
# carro.set_dono(dono)
# carro.set_modelo(modelo)
# print(carro.get_dono())
# print(carro.get_modelo())



#4
# class ContaBancaria():
#     def __init__(self, saldo):
#         self.__saldo = saldo

#     def get_saldo(self):
#         return self.__saldo
        
    
#     def set_saldo(self, saldo):
#         if isinstance(saldo ,float) and saldo >= 0:
#             self.__saldo = saldo
#         else:
#             print("Seu saldo nunca pode ser negativo!")

# saldo_inicial = 1000
# conta_bancaria = ContaBancaria(saldo_inicial)

# resposta = True
# while resposta != 'nao' or escolha != '3':

    
#     print(f"---Seja Bem Vindo!---\n- Seu saldo atual: R${conta_bancaria.get_saldo():.2f}\n1- Depósito\n2- Saque\n3- Sair")
#     escolha = input("O que será hoje: ")

#     if escolha == '1':
#         deposito = float(input("Valor a ser depositado: R$"))
#         if deposito < 0:
#              print("Depósito inválido!")
#         else:
#             saldo_atualizado = conta_bancaria.get_saldo() + deposito
#             conta_bancaria.set_saldo(saldo_atualizado)
#             print(f"Saldo atual: R${conta_bancaria.get_saldo():.2f}")

#     elif escolha == '2':
#             saque = float(input("Valor a ser sacado: R$"))
#             if saque > conta_bancaria.get_saldo():
#                 print(f"Você está tentando sacar mais dinheiro do que você possui! Calma lá!")
#             else: 
#                 saldo_atualizado = conta_bancaria.get_saldo() - saque
#                 conta_bancaria.set_saldo(saldo_atualizado)
#                 print(f"Saldo atual: R${conta_bancaria.get_saldo():.2f}")


#     elif escolha == '3':
#             print("Saindo...")

#     else:
#             print("Escolha um opção válida!")
        

#     if escolha == '3':
#          break

#     resposta = input("Deseja realizar outra ação(s/n): ").strip() .lower()
#     if resposta == 'n':
#         break



# 5
# class Aluno():
#     def __init__(self,nome_aluno, nota):
#         self.__nome_aluno = nome_aluno
#         self.__nota = nota

#     def get_nome_aluno (self):
#         return self.__nome_aluno
    
#     def set_aluno(self):
#         if isinstance (nome_aluno, str) and len(nome_aluno) > 0:
#             self.__nome_aluno = aluno
#         else:
#             print("Aluno inválido!")

#     def get_nota(self):
#         return self.__nota
    
#     def set_nota(self,nota):
#         if isinstance(nota, float):
#             self.__nota = nota

# resposta = 's'
# while resposta != 'n':
#     nome_aluno = input("Nome do aluno: ")
#     nota = float(input("Nota do aluno: "))
#     aluno = Aluno(nome_aluno, nota)
#     print(f"Aluno: {aluno.get_nome_aluno()}")
#     print(f"Nota: {aluno.get_nota()}")
#     resposta = input("Deseja definir a nota de outro aluno (s ou n): ")



# 6 
# class Produto():
#     def __init__(self, preco, nome_p):
#         self.__preco = preco
#         self.__nome_p = nome_p

#     def preco(self):
#         return self.__preco
    
#     def set_preco(self, preco):
#         if isinstance(preco, float) and len(preco) >= 0:
#             self.__preco = preco
#         else:
#             print("O valor do produto não pode ser negativo!")

#     def nome_p(self):
#         return self.__nome_p
    
#     def set_nome_p (self, nome_p):
#         if isinstance(nome_p, str) and len(nome_p) > 0:
#             self.__nome_p = nome_p
#         else:
#             print('Nome inválido!')


# nome_p = input("Nome do produto: ")
# preco = float(input("Insira o valor do produto: R$"))
# produto = Produto(preco, nome_p)
# print(f"O produto '{produto.nome_p()}' está custando: R${produto.preco()}")



# 7
# class Livro():
#     def __init__(self, titulo, autor):
#         self.__titulo = titulo
#         self.__autor = autor

#     def g_autor(self):
#         return self.__autor
#     def autor (self, autor):
#         if isinstance(autor, str) and len(autor) > 0:
#             self.__autor = autor
#         else:
#             print("Nome do autor inválido!")

#     def g_titulo(self):
#         return self.__titulo
#     def titulo(self, titulo):
#         if len(titulo) > 0:
#             self.__titulo = titulo
#         else:
#             print("Título inválido!")        

# autor = input("Autor: ")
# titulo = input("Título do livro: ")
# livro = Livro(autor, titulo)
# print(f"O livro {livro.g_autor()} foi criado pelo {livro.g_titulo()}")



# 8 
# class Funcionario():
#     def __init__(self,salario):
#         self.__salario = salario

#     def salario (self):
#         return self.__salario
#     def set_salario (self, salario):
#         if isinstance(salario, float) and len(salario) > 0 and salario > 0:
#             self.__salario = salario
#         else:
#             print("Salário inválido")
        
# salario_inicial = 1412.00
# print(f"-Salário atual: R${salario_inicial:.2f}")
# print("1- Adicionar aumento\n2- Abaixar salário\n3- Sair")
# escolha = input("Oque deseja fazer: ")
# if escolha == '1':
#     aumento = float(input("Aumento: R$"))
#     salario = salario_inicial + aumento
#     funcionario = Funcionario(salario)
#     print(f"O salario do seu funcionário é: R${funcionario.salario():.2f}")
# if escolha == '2':
#     abaixar = float(input("Quanto deseja diminuir: R$"))
#     if abaixar > salario_inicial:
#         print("ERRO!!!")
#     else:
#         salario = salario_inicial - abaixar
#         funcionario = Funcionario(salario)
#         print(f"O salario do seu funcionário é: R${funcionario.salario():.2f}")
# if escolha == '3':
#     print("Saindo...")



# 9
# class Casa():
#     def __init__(self, endereco, valor):
#         self.__endereco = endereco
#         self.__valor = valor

#     def endereco(self):
#         return self.__endereco
#     def set_endereco(self, endereco):
#         if len(endereco) > 0:
#             self.__endereco = endereco
#         else:
#             print("Endereço inválido!")
        
#     def valor(self):
#         return self.__valor
    
#     def set_valor(self, valor):
#         if isinstance(valor, float) and len(valor) > 0:
#             self.__valor = valor
#         else:
#             print("Valor inválido!")


# endereco = input("Endereço da propriedade: ")
# valor = float(input("Preço da propriedade: R$"))
# casa = Casa(endereco, valor)
# print(f"A casa se encontra no endereço: {casa.endereco()}\nEstá custando um valor de R${casa.valor():.2f}\nOu em ate 32x de R${(casa.valor() / 32) + 25:.2f}")



# 10 
# class Celular():
#     def __init__(self,marca):
#         self.__marca = marca

#     def marca(self):
#          return self.__marca
    
#     def set_marca (self, marca):
#            if len(marca) > 0:
#                 self.__marca = marca


# marca = input("Marca do celular: ")
# celular = Celular(marca)
# print(f"A marca do celular é {celular.marca()}")



# 11
# class Animal ():
#     def __init__(self, idade):
#         self.__idade = idade

#     def idade(self):
#         return self.__idade        
    
#     def set_idade(self,idade):
#         if isinstance(idade, int) and len(idade) > 0 and idade > 0:
#             self.__idade = idade
#         else:
#             print("Idade inválida!!!")


# idade = int(input("Idade do animal: "))
# animal = Animal(idade)
# print(f"Seu animal tem {animal.idade()} ano(s)")



# 12
# class Estudante():
#     def __init__(self, nome, matricula):
#         self.__nome = nome
#         self.__matricula = matricula

#     def nome(self):
#         return self.__nome
#     def matricula(self):
#         return self.__matricula

#     def set_nome(self,nome):
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nome = nome
#         else: 
#             print("Nome inválido!!")

#     def set_matricula(self,matricula):
#         if isinstance(matricula, int) and len(matricula) > 0:
#             self.__matricula = matricula
#         else:
#             print("Matrícula inválida!")        


# nome = input("Qual o nome do estudante: ")
# matricula = int(input("Número da matrícula: "))
# estudante = Estudante(nome, matricula)
# print(f"O número da matrícula do estudante {estudante.nome()} é {estudante.matricula():.0f}")



# 13
# class Veiculo():
#     def __init__(self, velocidade_max):
#         self.__velocidade_max = velocidade_max

#     def velocidade_max(self):
#         return self.__velocidade_max
    


# velocidade_max = float(input("Velocidade do veículo: "))
# veiculo = Veiculo(velocidade_max)
# print(f"A velocidade do veículo é {veiculo.velocidade_max()}km/h")

        

# 14
# class Computador():
#     def __init__(self, memoria_ram):
#         self.__memoria_ram = memoria_ram

#     def memoria_ram(self):
#         return self.__memoria_ram
    
#     def set_memoria_ram(self,memoria_ram):
#         if len(memoria_ram) > 0 and memoria_ram > 0:
#             self.__memoria_ram = memoria_ram
#         else:
#             print("Valor inválido para a memória RAM!")

# memoria_ram = int(input("Insira quantos GB tem sua memória RAM: "))
# computador = Computador(memoria_ram)
# print(f"Seu computador tem {computador.memoria_ram()}GB de RAM")



# 15
# class Curso():
#     def __init__(self, nome, duracao):
#         self.__nome = nome
#         self.__duracao = duracao

#     def nome(self):
#         return self.__nome
#     def duracao(self):
#         return self.__duracao
    
#     def set_nome(self, nome):
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nome = nome
#         else:
#             print("Nome inválido!")

#     def set_duracao(self, duracao):
#         if isinstance(duracao, float) and len(duracao) > 0:
#             self.__duracao = duracao
#         else:
#             print("Duração inválida!!")


# nome = input("Nome do curso: ")
# duracao = float(input("Duração do curso(em horas): "))
# curso = Curso(nome, duracao)
# print(f"O curso {curso.nome()} tem uma duração de {curso.duracao():.0f} horas")        



# 16
# class Jogo():
#     def __init__(self, pontuacao):
#         self.__pontuacao = pontuacao

#     def pontuacao(self):
#         return self.__pontuacao
    

# pontuacao = float(input("insira sua pontuação na partida: "))
# jogo = Jogo(pontuacao)
# print(f"Sua pontuação no jogo foi {jogo.pontuacao()} pontos")
        


# 17
# class Empresa():
#     def __init__(self, nome, numero_funcionarios):
#         self.__nome = nome
#         self.__numero_funcionarios = numero_funcionarios

#     def nome(self):
#         return self.__nome
#     def numero_funcionarios(self):
#         return self.__numero_funcionarios
    
#     def set_nome(self, nome):
#         if len(nome) > 0:
#             self.__nome = nome
#         else:
#             print("Nome de empresa inválida! ")

#     def set_numero_funcionarios(self, numero_funcionarios):
#         if isinstance(numero_funcionarios, int) and len(numero_funcionarios) > 0:
#             self.__numero_funcionarios = numero_funcionarios
#         else:
#             print("Número de funcionários inválido!")


# nome = input("Nome da Empresa: ")
# numero_funcionarios = int(input("Número de funcionários: "))
# empresa = Empresa(nome, numero_funcionarios)
# print(f"A empresa {empresa.nome()} tem {empresa.numero_funcionarios()} funcionários atualmente.")



# 18
# class Filme():
#     def __init__(self, titulo, ano):
#         self.__titulo = titulo
#         self.__ano = ano

#     def titulo(self):
#         return self.__titulo
#     def ano (self):
#         return self.__ano
    
#     def set_titulo(self, titulo):
#         if len(titulo) > 0:
#             self.__titulo = titulo
#         else:
#             print("Titulo inválido!")

#     def set_ano (self,ano):
#         if isinstance(ano, int) and len(ano) > 0:
#             self.__ano = ano
#         else:
#             print("Ano de lançamento inválido!")

# titulo = input("Titulo do filme: ")
# ano = int(input("Ano de lançamento: "))
# filme = Filme(titulo, ano)
# print(f"O filme {filme.ano()} foi lançado no ano de {filme.ano()}")                



# 19
# class Cidade():
#     def __init__(self, nome, populacao):
#         self.__nome = nome
#         self.__populacao = populacao

#     def nome(self):
#         return self.__nome
#     def populacao (self):
#         return self.__populacao
    
#     def set_nome(self, nome):
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nomenome = nome
#         else: 
#             print("Nome da cidade inválido!")

#     def set_populacao(self, populacao):
#         if isinstance(populacao, int) and len(populacao) > 0:
#             self.__populacao = populacao
#         else: 
#             print("População inválida!")


# nome = input("Nome da cidade: ")
# populacao = int(input("Quantidade de habitantes da cidade: "))
# cidade = Cidade(nome, populacao)
# print(f'A cidade {cidade.nome()} tem atualmente {cidade.populacao:.0f} habitantes.')



# 20
# class Professor():
#     def __init__(self, nome, disciplina):
#         self.__nome = nome
#         self.__disciplina = disciplina

#     def nome(self):
#         return self.__nome
#     def disciplina(self):
#         return self.__disciplina
    
#     def set_nome (self,nome):
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nome = nome
#         else:
#             print("Professor inválido!")

#     def set_disciplina(self, disciplina):
#         if isinstance(disciplina, str) and len(disciplina) > 0:
#             self.__disciplina = disciplina
#         else:
#             print("Disciplina inexistente!")


    

# nome = input('Insira o nome do professor: ')
# disciplina = input("Disciplina: ")
# professor = Professor(nome, disciplina)
# print(f'O professor(a) {professor.nome()} leciona a disciplina de {professor.disciplina()}')