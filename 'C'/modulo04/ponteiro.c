#include <stdio.h>

int main(void)
{
    // definição de ponteiro: Um ponteiro é uma VARIÁVEL capaz de armazenar um endereço de memória ou o endereço de outra variável.
    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
}
