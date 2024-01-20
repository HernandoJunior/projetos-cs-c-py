#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
    // CRIA UM ARQUIVO E ABRE O ARQUIVO
    FILE *file = fopen("fone.csv", "a");
    // SE O ARQUIVO FOR INEXISTENTE, RETORNA 1
    if(file == NULL)
    {
        return 1;
    }
    //CRIANDO A STRING DE NOME E NUMERO
    char *nome = get_string("Nome: ");
    char *numero = get_string("Numero: ");
    //IMPRIMINDO NOME E NUMERO EM NO ARQUIVO "FILE"
    fprintf(file, "%s , %s\n", nome, numero);
    //FECHANDO O ARQUIVO ABERTO
    fclose(file);
}
