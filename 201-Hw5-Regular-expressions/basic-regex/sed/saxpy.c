#include <stdio.h>
#include <stdlib.h>


/**
 * Generate a random float
 * @return random float
 */
float rand_float(void)
{
    float out = ((float) rand()) / ((float) (RAND_MAX));
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
        float a = rand_float() - 0.5f;
        float x = rand_float() - 0.5f;
        float y = rand_float() - 0.5f;
        float s = a * x + y; // hehe s=ax+y : SAXP(lus)Y

        // using SAXPY as our core operation
        printf("%f * %f + %f = %f\n",
               a, x, y, s);
    }

    return 0;
}
