metaCump = 0
comaEnt = 0
somaEnt = 0

for x in range(5):
    entDia = int(input("Informe o número de entregas hoje: "))
    if (entDia >= 100):
        metaCump = metaCump + 1
    somaEnt = somaEnt + entDia

mediaEnt = somaEnt // 5

print("Cumpriu a meta em {} dias".format(metaCump))
print("Média de entregas:",mediaEnt)
