#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;

    if (ac == 2) //O argumento tem de ser sempre igual a dois...
    {
        while (av[1][i])
        {
            if (i % 2 == 1) //Essa é a condição para verificar um número ímpar...
                write(1, &av[1][i], 1);
            i++;
        }
    }
    write(1, "\n", 1);
}