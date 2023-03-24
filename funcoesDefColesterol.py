def nivelColesterol(id,col):
  
  if (id <= 29):
    if (col <= 200):
      return "Normal"
    else:
      return "Alto"
  
  elif (id >= 30) and (id <= 39):
    if (col <= 225):
      return "Normal"
    else:
      return "Alto"
  
  elif (id >= 40) and (id <= 49):
    if (col <= 245):
      return "Normal"
    else:
      return "Alto"

  else:
    if (col <= 265):
      return "Normal"
    else:
      return "Alto"

x = int(input("Informe a idade: "))
y = int(input("Informe o colesterol: "))

print(nivelColesterol(x,y))
