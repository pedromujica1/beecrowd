#Positivos e média
#Beecrowd 1064

numeros = [float(input()) for i in range(6)]
numeros_positivos = [positives for positives in numeros if positives > 0]
media = sum(numeros_positivos) / len(numeros_positivos)
print(f'{len(numeros_positivos)} valores positivos')
print(f'{media:.1f}')
