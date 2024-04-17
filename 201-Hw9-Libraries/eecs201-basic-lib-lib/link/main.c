#include <stdio.h>

extern const char *do_thing(void);
int main(int argc, char *argv[])
{
    puts(do_thing());
    return 0;
}
