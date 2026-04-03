#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;

    if (ac == 2 && av[1][i] != '\0') //A parte "!= '\0'" é opcional...
    {
        while (av[1][i + 1]) //Aqui verifica o espaço vazio uma casa na frente por causa do "i + 1"
        {
            write(1, &av[1][i], 1);
            write(1, "   ", 3); //imprimir extamente os 3 espaços
            i++;
        }
        write(1, &av[1][i], 1); //imprimir o último caracter...
    }
    write(1, "\n", 1);
}