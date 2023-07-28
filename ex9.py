##3 formas diferentes de resolver um exercício que pede para imprimir apenas os números múltiplos de 3 entre os números que o usuário informou

#ex1
x = []

for i in range(8):
    num = int(input("Informe um número"))
    if(num % 3 == 0):
        x.append(num)
x.sort()
print(x)


#ex2
x = []

for i in range (4):
    n = int(input("Informe um número: "))
    x.append(n)

    if (x[i] % 3 == 0):
        print("Divisível por 3:", x[i])
 

#ex3   
x = []

for i in range(4):
    n = int(input("Informe um número: "))
    
    if(n % 3 == 0):
        x.append(n)

print("Divisíveis por 3:",x)
