#Crescente e Decrescente
#Beecrowd 1113

def verifica_ordem(x,y):
    if y>x:
        print('Crescente')
    else: print('Decrescente')


x = 1
y = 0
while x!=y:
    x, y = map(int, input().split())
    if y == x:
        break
    verifica_ordem(x,y)
