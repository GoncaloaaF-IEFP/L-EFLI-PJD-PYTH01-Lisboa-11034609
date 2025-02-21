#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int idade;
    char idade_str[10];
    while(1) {

        printf("Digite sua idade: ");
        scanf("%s", &idade_str);
        idade = atoi(idade_str);

        if(idade == -1) {
            break;
        }

        printf("%d\n", idade);

    }

    return 0;
}

