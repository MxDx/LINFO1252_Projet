#include "../headers/test-and-set.h"
#include <stdio.h>

int lock(int *tatas) {
    int ret;
    // Inline assembly that sets the value of ret to the current value of tatas,
    // and sets the value of tatas to 1.
    // while (*tatas == 1);
    
    asm("enter:;"
        "testl %1, %0;"
        "jnz enter;"

        "atomic:;"
        "xchg %0, %1;"
        "testl %1, %1;"
        "jnz atomic;"

        :"=m"(*tatas), "=a"(ret)
        :"a"(1), "m"(*tatas));

    return ret;
}

int unlock(int* tatas) {
    int ret;
    // Inline assembly that sets the value of ret to the current value of tatas,
    // and sets the value of tatas to 0.
    asm("xchg %0, %1;"

        :"=m"(*tatas), "=a"(ret)
        :"a"(0), "m"(*tatas));

    return ret;
}

int main() {


    return 0;
}