//
// Created by Gonçalo Feliciano on 06/02/2025.
//

// file com a implementação das funcs

int subtracao(int a, int b) {
    return a - b;
}

int soma(int a, int b) {
    return a + b;
}

int div(int a, int b) {
    return a / b;
}

int multiplicacao(int a, int b) {
    return a * b;
}

int myPow(int a, int b) {
    int res = 1;

    for (int i = 1; i <= b; i++) {
        res *= a;
    }

    return res;

}