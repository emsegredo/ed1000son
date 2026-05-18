#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0; // No dia de exame pode ser inicializado dessa forma, não faz mal...
    
    if (ac == 2) // O argumento tem de ser igual a 2 sempre...
    {
        while (av[1][i])
        {
            if (av[1][i] >= 'a' && av[1][i] <= 'z') //Verificar se o caracter é minúsculo...
                av[1][i] -= 32; //caso seja minúsculo, será transformado em maiúsculo

            else if (av[1][i] >= 'A' && av[1][i] <= 'Z')//Verificar se o caracter é maiúsculo...
                av[1][i] += 32; //caso seja maiúsculo, será transformado em minúsculo

            write(1, &av[1][i], 1);
            i++;
        }
    }
    write(1, "\n", 1);
    return (0);
}