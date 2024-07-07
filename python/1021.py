#Notas e Moedas
#Beecrowd 1021
notas = [100.00,50.00,20.00,10.00,5.00,2.00]
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]

cash = float(input())
aux = int(cash)
#FOR LOOP PARA DESCOBRIR AS NOTAS
print('NOTAS:')
for i in range(len(notas)):
    pass  
    num_notas =aux//notas[i]
    print(f"{num_notas:.0f} nota(s) de R$ {notas[i]:.2f}")
    new_value = aux -(num_notas * notas[i])
    aux = new_value

#FOR LOOP PARA DESCOBRIR AS MOEDAS
coins = round(cash- int(cash),2)
qtdade_coins = new_value+coins
aux2  = qtdade_coins
print('MOEDAS:')
for i in range(len(moedas)-1):
    num_moedas = aux2//moedas[i]
    print(f"{num_moedas:.0f} moeda(s) de R$ {moedas[i]:.2f}")
    value = aux2 -(num_moedas * moedas[i])
    coins_value = round(value,2)
    #print(coins_value)
    aux2 = coins_value
#PRINT COM A DIVISIÃO POR 0.01 PARA EVITAR ERRO
print(f'{aux2/moedas[5]:.0f} moeda(s) de R$ {moedas[5]:.2f}')
