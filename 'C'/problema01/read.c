#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Texto: ");
    int a = 0, b = 0, c = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (islower(s[i]) || isupper(s[i]))
        {
            a++;
        }
        else if (isblank(s[i]))
        {
            b++;
        }
        else if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            c++;
        }
    }

    float L = (b != 0) ? ((float) a / b) * 100 : 0;
    float t = (c != 0) ? ((float) b / c) * 100 : 0;
    float x = (0.0588 * L) - (0.296 * t) - 15.8;
    if (x >= 16)
    {
        printf("Grade: 16+\n");
    }
    else if (x > 1)
    {
        printf("Grade %f\n", x);
    }
    else
    {
        printf("Antes da grade 1\n");
    }
}

/*
vamos ter que usar o indice:
índice = 0,0588 * L - 0,296 * S - 15,8.
L= numero medio de letras por 100 palavras. (L/QNT DE PALAVRAS * 100 = MEDIA DE LETRAS)
S=  numero medio de frases por 100 palavras no texto (numero de sentenças / quantidade de palavras * 100)
382,14
7,14
*/
