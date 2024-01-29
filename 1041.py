#Coordenadas de um Ponto
#Beecrowd 1041

eixoX,eixoY = input().split()
eixoX,eixoY= float(eixoX),float(eixoY)

if eixoX == 0.0 and eixoY == 0.0:  print('Origem')
elif eixoX > 0 and eixoY > 0: print('Q1')
elif eixoX > 0 and eixoY < 0: print('Q4')
elif eixoX < 0 and eixoY > 0: print('Q2')
elif eixoX < 0 and eixoY < 0: print('Q3')
elif eixoX == 0.0: print('Eixo Y')
elif eixoY == 0.0: print('Eixo X')
