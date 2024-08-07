//Beecrowd 1079
//Médias Ponderadas

#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
  int test_cases;
  scanf("%d",&test_cases);
  float n1,n2,n3;
  for (int i = 0; i<test_cases; i++){
    scanf("%f %f %f", &n1, &n2, &n3);
    printf("%.1f\n",((n1*2)+(n2*3)+(n3*5))/(3+5+2));
  }

 
}
