setor = str.lower(input("Informe o setor: "))
tipIng = str.lower(input("Informe o tipo de ingresso: "))

if(tipIng == "inteira") and (setor == "platéia vip"):
  valorTotal = (5/100 * 350) + 350
  print("R$:",valorTotal)
elif(tipIng == "meia") and (setor == "platéia vip"):
  print("Tipo de ingresso inválido")
elif(tipIng == "inteira") and (setor == "cadeira"):
  valorTotal = (5/100 * 200) + 200
  print("R$:",valorTotal)
elif(tipIng == "meia") and (setor == "cadeira"):
  valorTotal = (5/100 * 200) + 200/2
  print("R$:",valorTotal)
elif(tipIng == "inteira") and (setor == "arquibancada"):
  valorTotal = (5/100 * 100) + 100
  print("R$:",valorTotal)
elif(tipIng == "meia") and (setor == "arquibancada"):
  valorTotal = (5/100 * 100) + 100/2
  print("R$:",valorTotal)
else:
  print("Setor inválido")
