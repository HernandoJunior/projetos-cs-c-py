#include <stdio.h>
#include <string.h>

int main(void)
{
    // definição de string em 'C'. o (asterisco) está marcando o endereço de s.
    char *s = "HI!";
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);

    return 0;
}
