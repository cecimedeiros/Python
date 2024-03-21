class Carro:
  def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano
      self.velocidade = 0

  def acelerar(self, incremento):
      self.velocidade += incremento

  def frear(self, decremento):
      self.velocidade -= decremento
      if self.velocidade < 0:
          self.velocidade = 0

  def imprimir_informacoes(self):
      print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade}")
