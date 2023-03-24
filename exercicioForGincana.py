vLCC = 0
vSI = 0
emp = 0
venc = 0

for i in range(5):
    
    lcc = int(input("Informe pontuação da rodada de LCC: "))
    si = int(input("Informe pontuação da rodada de BSI: "))

    if(lcc > si):
        vLCC += 1
    elif(lcc == si):
        emp += 1
    else:
        vSI += 1

if(vLCC > vSI):
    venc = "LCC"
else:
    venc = "BSI"
print("Vitórias LCC:",vLCC)
print("Vitórias BSI:",vSI)
print("Empates:",emp)
print(venc)
