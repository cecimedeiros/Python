#informa os números entre um intervalo crescente informado pelo usuário

print("Informe o intervalo:")
x = int(input())
y = int(input())
if (x > y):
      print("intervalo inválido")

for z in range(x + 1,y):
    print(z)
