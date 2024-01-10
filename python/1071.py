#Soma de Impares Consecutivos I
#Beecrowd 1071

def verificacao_impares(x,y):
    temp=0

    for numeros in range(y+1,x):
        if numeros%2 ==0:
            temp+=0
        else:
            temp+=numeros
    return temp
    

x,y = int(input()), int(input())
print(verificacao_impares(x,y))
