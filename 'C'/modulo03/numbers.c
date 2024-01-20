#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{ // lendo uma string de numeros já definidos
    int number[] = {4, 6, 8, 2, 7, 5, 0};

    for (int i = 0; i < 7; i++)
    { // procurando um numero dentro da string
        if (number[i] == 0)
        {
            printf("Numero encontrado\n");
            return 0;
        }
    }
    printf("Numero nao encontrado");
    return 1;
}

/*
RETURN 0 = SAIA DO PROGRAMA PORQUE ESTÁ TUDO CERTO;
RETURN 1 = ALGO DEU ERRADO MAS O PROGRAMA FOI FINALIZADO;
*/
