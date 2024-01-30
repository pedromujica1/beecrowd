#Intervalo 2
#Beecrowd 1072

count_in = 0
count_out = 0

for i in range(int(input())):
    n = int(input())
    
    if n <10 or n>20:
        count_out+=1
    if n>=10 and n<=20:
        count_in+=1
print(f'{count_in} in')
print(f'{count_out} out')
