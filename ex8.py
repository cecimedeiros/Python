#informa o menor entre 5 números informados pelo usuário

lista = []

for x in range(5):
    lista.append(int(input("Informe um número: ")))

lista.sort()
lista[0]
