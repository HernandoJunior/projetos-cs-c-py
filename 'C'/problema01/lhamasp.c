#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //entrada de dados da população total de lhamas
    int lhamas;
    do
    {
        lhamas = get_int("População de lhamas: ");
    }
    while(lhamas < 1);

    //tamanho inicial de lhamas que nasceram no ano
    int inicial;
    do
    {
        inicial = get_int("Tamanho inicial: ");
    }
    while(inicial < 1);
    int i = lhamas / inicial;

    //tamanho final das lhamas que restaram
    int final;
    do
    {
        final = get_int("Tamanho final: ");
    }
    while(final < inicial || final < 1);

    int j = lhamas / final;

    int f = lhamas + i - j;

    printf("Years: %d\n", f);

}
