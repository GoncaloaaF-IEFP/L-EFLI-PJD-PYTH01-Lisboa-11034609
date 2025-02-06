#include <stdio.h>
int sumatorio(int x);
int sumatorio_recur(int x);


int main(void) {
   int res = sumatorio(5); // 15
    printf("o sumatorio é: %d\n", res);

    int res2 = sumatorio_recur(5); // 15
    printf("o sumatorio_recur é: %d\n", res2);


   return 0;
}


int sumatorio(int x){
    int sum = 0;

    for(int i = 1; i <= x; i++){
        sum += i;
    }
    return  sum;

}


int sumatorio_recur(int x){

    if (x == 1){
        return 1;
    }
    return x + sumatorio_recur(x-1);

}