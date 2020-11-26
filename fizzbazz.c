#include <stdio.h>

int main(void) {
    int i;
    char ans[20]
    for (i = 0; i <= 20; i++) {
        if (i % 5 == 0 && i % 3 == 0){
            printf("Fizz Buzz\n");
        } else if (i % 3 == 0) {
            printf("Fizz\n");
        } else if (i % 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%d\n", i);
        }
    };
    return 0;
};
