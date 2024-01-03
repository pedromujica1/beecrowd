#Teste de seleção 1
#Beecrowd 1035
def verifica_numeros(num1,num2):
    if (num1 > 0) and (num2 >0):
        return True
    return False
def verificar_par(num):
    if num%2 == 0:
        return True
    return False

numeros = list(map(int, input().split()))
somaCD=numeros[2]+numeros[3]
somaAB =numeros[0]+numeros[1]
if (numeros[1] > numeros[2]) and (numeros[3] > numeros[0]) and (somaCD > somaAB) and (verifica_numeros(numeros[2],numeros[3])) and (verificar_par(numeros[0])):
    print('Valores aceitos')
else: print('Valores nao aceitos')
    
