#include <stdio.h>
/*
 *
 * Inicio

    altura   Ler inteiro

    para linha <— 1 ate altura com incremento 1 fazer

		Para col <— 1 ate Altura - linha com incremento 1 fazer
			escrever “#”
		fimPara

		Para col <— 1 ate  linha com incremento 1 fazer
			escrever “*”
		fimPara

	mudar_linha

	fimPara

Fim

 */

void piramidDir();

int main() {

    piramidDir();

    return 0;
}


void piramidDir(){
    int altura;
    printf("Altura: ");
    scanf("%d", &altura);


    for(int linha = 1; linha <= altura; linha++ ) {

        /*
         * 	Para col <— 1 ate Altura - linha com incremento 1 fazer
			    escrever “#”
		    fimPara
         */
        for(int col = 1; col <= (altura-linha); col++){
            printf(" ");
        }

        /*
         * 	Para col <— 1 ate  linha com incremento 1 fazer
			    escrever “*”
		    fimPara
         */

        for(int col = 1; col <= linha; col++){
            printf("*");
        }

        printf("\n");
    }


}