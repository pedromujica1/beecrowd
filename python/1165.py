#Beecrowd 1165 - Número Primo
def numero_primo(n):
    #Contador divisiveis
    cont_divisiveis=0
    for i in range(1,n+1): 
        if n%i ==0:
            cont_divisiveis +=1
    if cont_divisiveis == 2:
        return f'{n} eh primo'
    return f'{n} nao eh primo'

#Entradas de dados
for j in range(int(input())):
    number = int(input())
    print(numero_primo(number))
