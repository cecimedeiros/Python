{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Carro:\n",
    "    def __init__(self, marca, modelo):\n",
    "        self.marca = marca\n",
    "        self.modelo = modelo\n",
    "        self.velocidade = 0\n",
    "\n",
    "    def acelerar(self):\n",
    "        self.velocidade += 10\n",
    "        print(f\"O carro {self.marca} {self.modelo} está acelerando. Velocidade: {self.velocidade} km/h\")\n",
    "\n",
    "    def frear(self):\n",
    "        self.velocidade -= 5\n",
    "        print(f\"O carro {self.marca} {self.modelo} está freando. Velocidade: {self.velocidade} km/h\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O carro Toyota Corolla está acelerando. Velocidade: 10 km/h\n",
      "O carro Toyota Corolla está freando. Velocidade: 5 km/h\n"
     ]
    }
   ],
   "source": [
    "# Criando uma instância da classe Carro\n",
    "meu_carro = Carro(marca=\"Toyota\", modelo=\"Corolla\")\n",
    "\n",
    "# Chamando métodos da instância\n",
    "meu_carro.acelerar()\n",
    "meu_carro.frear()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
