#include <cs50.h>
#include <stdio.h>
#include <string.h>

//função para definir o tipo de array
typedef struct
{
    string nome;
    string numero;
}
person;

int main(void)
{
    person pessoa[2];
    pessoa[0].nome = "Hernando";
    pessoa[0].numero = "(71) 9.9741-5316";

    pessoa[1].nome = "Amanda";
    pessoa[1].numero = "(71) 9.9697-1012";

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(pessoa[i].nome, "Hernando") == 0)
        {
            printf("Encontrei %s\n", pessoa[i].numero);
            return 0;
        }
    }
    printf("Não encontrado");
    return 1;
}
