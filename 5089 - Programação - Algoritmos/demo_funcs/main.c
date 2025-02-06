#include <stdio.h>


void myFunc();
void myFunc2(int ano);
int soma(int v1, int v2);


int main() {

    int num = 10;

    int res = num % 2; // -> 0

    num = 11;
    res = num % 2; // -> 1


    /*
     *  11 / 2
     *
     *  5
     *  resto - 1
     */

    myFunc2(2024);
    myFunc2(2025);
    myFunc2(2026);

    if (-1) {
        printf("v1\n");
    }else{
        printf("v2\n");
    }

    int mySoma = soma(10,12);

    printf("A soma é %d\n", mySoma);





    return 0;
}



void myFunc(){
    printf("Ola Mundo\n");
}

void myFunc2(int ano){
    printf("Ola Mundo, %d\n", ano);
}

int soma(int v1, int v2){
    int r = v1 + v2;
    return r;

}

