#include <stdio.h>
#include <stdlib.h>


/**
 * Generate a random float
 * @return random float
 */
double rand_double(void)
{
    double out = ((double) rand()) / ((double) (RAND_MAX));
    return out;
}

int main(int argc, char *argv[])
{
    int i;
    // print a welcome message
    printf("Hello world!\n");

    // perform some math
    for (i = 0; i < 10; ++i) {
        // get some random numbers
        // from -0.5 to +0.5
        double a = rand_double() - 0.5f;
        double x = rand_double() - 0.5f;
        double y = rand_double() - 0.5f;
        double d = a * x + y; // hehe d=ax+y : DAXP(lus)Y

        // using DAXPY as our core operation
        printf("%g * %g + %g = %g\n",
               a, x, y, d);
    }

    return 0;
}
