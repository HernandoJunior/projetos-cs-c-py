#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    // na string t, estou pegando a localizaçao de s e o comprimento até o caractere null
    char *t = malloc(strlen(s) + 1);
    /*// direcionando a string s para t
    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }

    t[0] = toupper(t[0]);
    */
   // copiando uma string para outra
    strcpy(t, s);

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    free(t);

}
