#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* Calculate 2**1000 and finds the sum of all digits */

int main(void)
{
    double num = pow(2, 1000);
    int number_of_digits = log10(num) + 1;
    char num_string[number_of_digits];

    sprintf(num_string, "%f", num);

    int digits_sum = 0;
    char *c = num_string;
    while (*c != '.')
    {
        digits_sum += *c - '0';
        c++;
    }

    printf("sum of digits %d\n", digits_sum);

    return 0;
}
