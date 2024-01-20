#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");
    // comparando duas strings
    if (strcmp(s, t) == 0)
    {
        printf("Iguais\n");
    }
    else
    {
        printf("Diferentes\n");
    }
    return 0;
}
