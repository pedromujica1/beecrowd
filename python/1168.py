#LED
#Beecrowd 1168

leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#6, 2, 5, 5, 4, 5, 6, 3, 7, 6

#PERCORRER TESTES DE CASOS
for i in range (int(input())):
    count_leds = []
    user = input().strip()

    str_input = list(''.join(user ))
    #PERCORRER A LISTA DE VALORES
    for i in range(len(str_input)):
        led = leds[ int(str_input[i]) ]
        count_leds.append(led)
    print(f'{sum(count_leds)} leds')
    count_leds = []
