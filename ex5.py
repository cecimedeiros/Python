#exercicio usando def que recebe a idade de um aluno e o curso que ele deseja após isso informa mensalidade, caso o aluno possa participar do curso

def mensalidade(x,y):
 
    if(x == "natação"):
        mens = 60
        if (y <= 12):
            tt = mens / 2
            return tt
        elif (y >= 65):
            tt = mens - (mens * 0.3)
            return tt
        else:
            return mens

    elif(x == "dança"):
        mens = 80
        if (y <= 12):
            tt = mens / 2
            return tt
        elif (y >= 65):
            tt = mens - (mens * 0.3)
            return tt
        else:
            return mens    
            
    elif(x == "pilates"):
        mens = 70
        if (y <= 12):
            return "0, Crianças não participam de pilates"
        elif (y >= 65):
            tt = mens - (mens * 0.3)
            return tt
        else:
            return mens
            

curso = str.lower(input("Informe o curso: "))
idade = int(input("Informe a idade: "))

print(mensalidade(curso,idade))
