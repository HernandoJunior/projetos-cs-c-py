#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    string s = get_string("Entrada: ");
    printf("Saída:  ");
    for(int i = 0; s[i] != '\0'; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");

}
