#Formula de Bhaskara
#Becrowd 1036

valA,valB,valC =input().split()
valA,valB,valC = float(valA),float(valB),float(valC)

#x1 = (-b+(0.5**(b**2 -(4*a*c))))/2*a
#x2 = (-b-(0.5**(b**2-(4*a*c))))/2*a
try:
    delta_equation = valB**2 - (4*valA*valC)
    if delta_equation>0:
        raiz_x1 = (-valB+(delta_equation**0.5)) / (2*valA)
        raiz_x2 = (-valB-(delta_equation**0.5)) / (2*valA)
        print(f'R1 = {raiz_x1:.5f}')
        print(f'R2 = {raiz_x2:.5f}')
    else:
        print('Impossivel calcular')
except ZeroDivisionError as e:
    print('Impossivel calcular')
