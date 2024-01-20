#include <stdio.h>
#include <stdlib.h>
// prototipo da função
void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x é igual: %i, y é igual: %i\n", x, y);
    swap(&x, &y);
    printf("x é igual: %i, y é igual: %i\n", x, y);
}
// inversao de valores
void swap(int *a, int *b)
{
    int x = *a;
    *a = *b;
    *b = x;
}
