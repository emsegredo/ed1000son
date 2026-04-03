#include <unistd.h>

void ft_print_number(int numero)
{
    if (numero > 9)
        ft_print_number(numero / 10);
    write(1, &"0123456789"[numero % 10], 1);
}

int main(void)
{
    int numero = 1;

    while (numero <= 100)
    {
        if (numero % 3 == 0 && numero % 5 == 0)
            write(1, "fizzbuzz", 8);
        else if (numero % 5 == 0)
            write(1, "buzz", 4);
        else if (numero % 3 == 0)
            write(1, "fizz", 4);
        else
            ft_print_number(numero);
        write(1, "\n", 1);
        numero++;
    }
}