//Becrowd 1175
//Troca em Vetor I
#include <stdio.h>

int main(){
    int numeros[20];
    int index= 0;
    for (int i = 0; i < 20; i++)
    {
        scanf("%d",&numeros[i]);
    }
    for (int i = 19; i >= 0; i--)
    {
        printf("N[%d] = %d\n",index,numeros[i]);
        index++;
    }
    
    
}