#include <stdio.h>
void showData(int data[], int size);


int main(void) {
    int notas[] = {1,2,3,5,6};
    printf("%d\n", notas[4]);
    notas[4] = 9;
    printf("%d\n", notas[4]);


    int notas2[5];
    // 0, 1, 2, 3, 4


    printf("%d\n", notas2[3]);
    notas2[3] = 21;
    printf("%d\n", notas2[3]);

    /*
    printf("----------\n");
    printf("%d\n", notas2[8]);
    notas2[8] = 21; // <- incorrecto
    printf("%d\n", notas2[8]);
*/
    int x;
    float y;
    double z;

    printf("----------\n");
    char c1 = 'o';
    char c2 = 'l';
    char c3 = 'a';


    printf("%c%c%c\n", c1,c2,c3);


    char msg[4] = "Ola";
    printf("%s\n", msg);
    printf("teste\n");

    printf("----------\n");
    printf("----------\n");

    showData(notas, 5);

    printf("----------\n");
    printf("----------\n");


    int s = sizeof(notas) / sizeof(notas[0]);

    printf("%d\n", s);
    return 0;
}




void showData(int myData[], int size){

    for(int i = 0; i < size; i++){

        printf("nota %d: %d\n",i+1, myData[i]);

    }

}


/*
 *  i = 1
 *
 *  i++ <--> i = i + 1 --> i = 2
 *
 *  i += 1 <--> i = i + 1 --> i = 2
 *
 *
 * i + 1 --> i = 1
 */