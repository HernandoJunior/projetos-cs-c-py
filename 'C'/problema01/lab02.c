#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int agrv, char *argv[])
{
    if (agrv == 2 || atoi(argv[1]) != 26)
    {
        printf("A chave deve conter 26 caracteres \n");
        return 1;
    }
    else
    {
        int chave = atoi(argv[1]);
        string s = get_string("Texto simples: ");
        printf("Texto cifrado: ");
        for (int i = 0, n = strlen(s); i < n; i++)
        {
            if (isalpha(s[i])) // Verifica se o caractere é uma letra
            {
                if (islower(s[i])) // Verifica se é uma letra minúscula
                {
                    s[i] = 'a' + (s[i] - 'a' + chave) % 26;
                }
                else // É uma letra maiúscula
                {
                    s[i] = 'A' + (s[i] - 'A' + chave) % 26;
                }
            }

            printf("%c", s[i]);
        }

        printf("\n");
        return 0;
    }
}
