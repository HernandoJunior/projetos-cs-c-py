#include <stdio.h>
#include <cs50.h>

//DECLARAR A FUNÇÃO ANTES DO INICIO DO PROGRAMA
int get_negative_int(void);

int main(void)
{
    int i = get_negative_int();
    printf("%d\n", i);

}

//FUNÇOES
int get_negative_int(void)
{
    int n;
    do
    {
        n = get_int("Escreva um numero negativo ");
    }
    while(n > 0);
    return n;
}
