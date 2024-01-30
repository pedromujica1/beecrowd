#PUM
#Beecrowd 1142

test_cases = int(input())
linhas = []

for i in range (1,(test_cases*4)+1):
    if i%4 ==0:
        string = f'{i-3} {i-2} {i-1} PUM'
        linhas.append(string)
for i in range(len(linhas)): print(linhas[i])
