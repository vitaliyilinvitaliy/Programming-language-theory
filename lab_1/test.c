#include <stdlib.h>

struct test{
    char name[15];
    char age;
};

int main()
{
    struct test *test_str = malloc(sizeof(struct test));
    
    char age = test_str->age;



}
