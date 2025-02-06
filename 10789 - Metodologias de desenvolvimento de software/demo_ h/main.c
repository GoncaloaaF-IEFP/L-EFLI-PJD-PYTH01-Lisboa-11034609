#include <stdio.h>



void ola_Mundo(char nome[]) {
    printf("Ola Mundo, %s\n", nome);
}

void isAdulto(int idade) {

    if (idade >= 18) {
        printf("Is Adulto\n");
    }else {
        printf("Is not Adulto\n");
    }
}

void isAdultoV2(char nome[], int idade) {

    if (idade >= 18) {
        printf("ola %s, já es adulto\n", nome);
    }else {
        int dif = 18 - idade;
        printf("ola %s,faltam %d anos para seres adulto\n", nome, dif);
    }
}

int main(void) {
    ola_Mundo("Gonçalo");
    ola_Mundo("Joao");
    ola_Mundo("Carlos");
    ola_Mundo("Ana");
    ola_Mundo("Rui");

    isAdulto(18);
    isAdulto(15);

    isAdultoV2( "Joao", 18);

    isAdultoV2( "Rita", 17);
    isAdultoV2( "Rita", 16);
    return 0;
}




