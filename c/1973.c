//Beecrowd 2466
//Sinuca
#include <stdio.h>
#include <stdlib.h>

int main(){
    //Variaveis
    int qtdade_estrelas;
    scanf("%d",&qtdade_estrelas);
    int carneiros[qtdade_estrelas];
    int carneiros_vivos[qtdade_estrelas];
    

    //Entrada de dados
    for (int i = 0; i < qtdade_estrelas; i++) {
        scanf("%d", &carneiros[i]);
    }
    int pos_par= 0;
    int estrelas = 0;
    int soma_ovelhas=0;
    for (int i = 0; i < qtdade_estrelas; i++) {
        if (carneiros[i] %2 ==0){
            pos_par = i;
            estrelas++;
        }
    }
    for (int i = 0; i < pos_par; i++){
        if (carneiros[i]%2 ==1){
            carneiros[i] -=1;
            estrelas++;
        } 
    }
    for (int i = 0; i < pos_par-1; i++){
        if (carneiros[i]%2 ==0){
            carneiros[i] -=1;
        } 
    }

    for (int i = 0; i<qtdade_estrelas; i++){
        soma_ovelhas+=carneiros[i];
    }
    printf("%d %d\n",soma_ovelhas,estrelas);



    

    
    // //Saida de dados
    // if (retorno == 0){
    //     printf("%d %d\n",estrelas_invadidas,carneiros_salvos);
    // }
    // else{
    //     printf("%d %d\n",estrelas_invadidas,carneiros_salvos+retorno);
    // }
    return 0;
}