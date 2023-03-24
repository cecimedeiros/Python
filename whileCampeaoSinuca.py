quantComp = 0
maiorPont = 0

nome = input("Informe o nome do competidor: ")
pont = int(input("Informe a pontuação: "))

while(quantComp < 3):
  if(pont > maiorPont):
    maiorPont = pont
    nomeVenc = nome
  nome = input("Informe o nome do competidor: ")
  pont = int(input("Informe a pontuação: "))
  if(pont > maiorPont):
    maiorPont = pont
    nomeVenc = nome
  quantComp = quantComp + 1

print("{0} venceu a competição com {1} pontos".format(nomeVenc, maiorPont))
