#Pares entre cinco números
#Beecrowd 1065

numeros = [int(input()) for i in range(5)]
numeros_pares = [nums for nums in numeros if nums%2 == 0]
print(f'{len(numeros_pares)} valores pares')
#positives for positives in numeros if positives > 0
