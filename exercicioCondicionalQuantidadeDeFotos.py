qtdeFotos = int (input('Quantas fotos para revelar? '))
if (qtdeFotos <= 0):
  print('Informe uma quantidade válida')
else:
  if (qtdeFotos <= 30):
    precoFoto = 0.69
  elif (qtdeFotos <= 50):
    precoFoto = 0.59
  elif (qtdeFotos <= 100):
    precoFoto = 0.49
  else:
    precoFoto = 0.39
  total = precoFoto * qtdeFotos
  print ('O custo total da revelação é', total)
  if (qtdeFotos > 200):
    print ('Você ganhou um álbum')
