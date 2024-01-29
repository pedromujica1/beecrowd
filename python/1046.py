#Tempo de jogo
#Beecrowd 1046

hora_ini, hora_fim = input().split()
hora_ini, hora_fim = int(hora_ini),int(hora_fim)
duracao = 0
if hora_ini == hora_fim:
    duracao = 24
    print(f'O JOGO DUROU {duracao} HORA(S)')
    

elif hora_ini>12:
    hora_ini = 24-hora_ini
    duracao = hora_ini+hora_fim
    print(f'O JOGO DUROU {duracao} HORA(S)')
    
else:
    duracao = hora_fim- hora_ini 
    print(f'O JOGO DUROU {duracao} HORA(S)')
