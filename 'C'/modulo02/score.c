#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);
float media(int quant, int array[]);

int main(void)
{
    int scores[99];
    int N = get_positive_int();
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Digite a %d nota: ", i + 1);
    }

    printf("Media de %.2f\n", media(N, scores));
}

// FUNÇÕES
// LEIA QUANTOS NUMEROS O HUMANO VAI DIGITAR
int get_positive_int(void)
{
    int a;
    do
    {
        a = get_int("Quantas notas voce vai digitar: ");
    }
    while (a <= 1);
    return a;
}

// FUNCAO PARA CALCULAR A MEDIA DAS NOTAS
float media(int quant, int array[])
{
    int sum = 0;
    for (int i = 0; i < quant; i++)
    {
        sum += array[i];
    }
    return sum / (float) quant;
}
