#include <stdint.h>
#include <stdio.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Verificar se o usuario digitou dois argumentos
    if (argc != 2)
    {
        return 1;
    }
    // Abrir o arquivo e ler o arquivo
    FILE *file = fopen(argv[1], "r");
    // verifica se o arquivo é nulo
    if (!file)
    {
        return 1;
    }
    // Ler os primeiros 3 bytes do array
    BYTE bytes[3];
    fread/*vai ler os bytes do arquivo*/(bytes, sizeof(BYTE), 3, file);
    // Verificar os três primeiros bytes
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Talvez\n");
    }
    else
    {
       printf("Não\n");
    }
    // Fechar o arquivo
    fclose(file);
}
