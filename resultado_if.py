sim = True
nao = False
trabalho_terca = eval(input("Conseguiu o trabalho na terça? sim ou nao: "))
trabalho_quinta = eval(input("Conseguiu o trabalho na quinta? sim ou nao: "))

if (trabalho_terca == True) and (trabalho_quinta == True):
  conquista = "casquinha e uma Tv 85'"
  print(trabalho_terca, "\n",trabalho_quinta)
  print("Você conquistou", conquista)

elif trabalho_terca == False and trabalho_quinta == True:
  conquista1 = "casquinha e uma Tv 32'"
  print(trabalho_terca, "\n",trabalho_quinta)
  print("Você conquistou", conquista1)

elif trabalho_terca == True and trabalho_quinta == False:
  conquista2 = "casquinha e uma Tv 32'"
  print(trabalho_terca, "\n",trabalho_quinta)
  print("Você conquistou", conquista2)

elif trabalho_terca == False and trabalho_quinta == False:
  conquista3 = "vida saudável"
  print(trabalho_terca, "\n",trabalho_quinta)
  print("Você conquistou", conquista3)

else:
  print("Responda com sim ou nao!")