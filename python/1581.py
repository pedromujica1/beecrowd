#Conversa internacional
#Beecrowd 1581

for i in range(int(input())):
    num_idiomas = int(input())
    idiomas = []
    for i in range(num_idiomas):
        idioma = str(input())
        idiomas.append(idioma)
     
        
    conjunto_idiomas = set(idiomas)
    if len(conjunto_idiomas) > 1:
        print('ingles')
    else: print(idiomas[0])
