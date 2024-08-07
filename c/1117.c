//Validação de Nota 
//Beecrowd 1117
#include <stdio.h>

int main()
{
    float notas;
    float notas_validas = 0.0;
    int qtdade_validas =1;
    while (qtdade_validas<=2){
        scanf("%f",&notas);
        if (notas <=10 && notas>=0){
            qtdade_validas++;
            notas_validas+=notas;
        }
        else{
            printf("nota invalida\n");
        }
    }
    printf("media = %.2f\n",notas_validas/2);

    return 0;
}