//Beecrowd 2466
//Sinuca
#include <stdio.h>
#include <stdlib.h>

int main(){
    int N;
    //Quantidade de bolas
    scanf("%d",&N);
    int bolas[N];
    int permutacoes = 0;

    //Classificação das bolas
    for (int i = 0; i < N; i++) {
        scanf("%d", &bolas[i]);
        permutacoes+=i;
    }
    printf("PERMUTACOES %d\n",permutacoes);
    int cont_brancas = 0;
    int cont_pretas = 0;
    for (int i = 0; i < permutacoes; i++) {
        //printf("%d", bolas[i]);
        if (bolas[i] != bolas[i+1]) {
            bolas[i]+=1;
        } if (bolas[i] == bolas[i+1]) {
            bolas[i]+=1;
        }
    
    }
    //for loop in bolas array
    for (int i = 0; i < N-1; i++)
    {
        printf("%d ", i);
        /* code */
    }
    
    printf("ULTIMA BOLA %d\n",bolas[0]);

    //condition ? expression_if_true : expression_if_false;

    //printf("\n%d BRANCAS", abs(cont_brancas));
    //printf("\n%d PRETAS", cont_pretas);

    
    return 0;
}