#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string nomes [] = {"Hernando", "Amanda"};
    string numeros [] = {"(71) 9.9741-5316", "(71) 9.9697-1012"};

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(nomes[i], "Hernando") == 0)
        {
            printf("Encontrei %s\n", numeros[i]);
            return 0;
        }
    }
    printf("Não encontrado");
    return 1;
}
