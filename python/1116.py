#1116 - Dividindo X por Y 
for i in range(int(input())):
    try:   
        a,b = map(int,input().split())
        print(a/b)
    except ZeroDivisionError:
        print("divisao impossivel")
