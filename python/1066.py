#Pares, Ímpares, Positivos e Negativos
#Beecrowd 1066

numeros = [int(input()) for i in range(5)]
numeros_pares = [nums for nums in numeros if nums%2 == 0]
numeros_impares = [nums for nums in numeros if nums%2 != 0]
numeros_positivos = [nums for nums in numeros if nums>0]
numeros_negativos = [nums for nums in numeros if nums<0]
print(f'{len(numeros_pares)} valor(es) par(es)')
print(f'{len(numeros_impares)} valor(es) impar(es)')
print(f'{len(numeros_positivos)} valor(es) positivo(s)')
print(f'{len(numeros_negativos)} valor(es) negativo(s)')
