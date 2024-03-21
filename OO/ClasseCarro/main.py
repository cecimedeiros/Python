from Carro import Carro
def main():
  # Criando uma instância da classe Carro
  meu_carro = Carro("Toyota", "Corolla", 2020)

  # Imprimindo as informações iniciais do carro
  meu_carro.imprimir_informacoes()

  # Acelerando o carro
  meu_carro.acelerar(50)

  # Imprimindo as informações após acelerar
  meu_carro.imprimir_informacoes()

  # Freando o carro
  meu_carro.frear(20)

  # Imprimindo as informações após frear
  meu_carro.imprimir_informacoes()

if __name__ == "__main__":
  main()
