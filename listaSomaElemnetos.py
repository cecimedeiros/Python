x = []
y = []
atual = 0

for i in range(5):
    num = int(input())
    x.append(num)
    if len(x) > 1:
        y.append(num + atual)
    atual = num
print(x)
print(y)
