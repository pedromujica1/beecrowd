#TDA racional
#Beecrowd 1022

def calcular_mdc(a, b):
  if b == 0: return a 
  else: return calcular_mdc(b, (a % b))

def simplifica_fracao(numerador,denominador,divisor):
    numerador_simp = numerador//divisor
    denominador_simp = denominador//divisor
    
    simplificado = f'{numerador_simp}/{denominador_simp}'
    return simplificado
    
#Soma: (N1*D2 + N2*D1) / (D1*D2)
#Subtração: (N1*D2 - N2*D1) / (D1*D2)

for i in range (int(input())):
    operacao = input().split()
    
    if operacao[3] == '+':
        
        numerador = (int(operacao[0]) * int(operacao[6]) + (int(operacao[2]) * int(operacao[4])))
        denominador = int(operacao[2]) *int(operacao[6])
        
        #CHAMANDO FUNÇOES
        maximo_divisor = calcular_mdc(numerador,denominador)
        fracao_nova = simplifica_fracao(numerador,denominador,maximo_divisor)
        print(f'{numerador}/{denominador} = {fracao_nova}')
    elif operacao[3] == '-':
        
        numerador = (int(operacao[0]) * int(operacao[6]) - (int(operacao[2]) * int(operacao[4])))
        denominador = int(operacao[2]) *int(operacao[6])
        
        maximo_divisor = calcular_mdc(numerador,denominador)
        fracao_nova = simplifica_fracao(numerador,denominador,maximo_divisor)
        print(f'{numerador}/{denominador} = {fracao_nova}')
    #Multiplicação: (N1*N2) / (D1*D2)
    #Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
    elif operacao[3] == '*':
    
        numerador = (int(operacao[0]) *int(operacao[4])) 
        denominador = int(operacao[2]) *int(operacao[6])
        
        maximo_divisor = calcular_mdc(numerador,denominador)
        fracao_nova = simplifica_fracao(numerador,denominador,maximo_divisor)
        print(f'{numerador}/{denominador} = {fracao_nova}')
        
    elif operacao[3] == '/':
        numerador = (int(operacao[0]) *int(operacao[6])) 
        denominador = (int(operacao[4]) *int(operacao[2]))
        
        maximo_divisor = calcular_mdc(numerador,denominador)
        fracao_nova = simplifica_fracao(numerador,denominador,maximo_divisor)
        print(f'{numerador}/{denominador} = {fracao_nova}')
