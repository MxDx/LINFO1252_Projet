#include "../headers/test-and-set.h"

int lock(int *tas) {
    int ret;
    // Inline assembly that sets the value of ret to the current value of tas,
    // and sets the value of tas to 1.
    asm("enter:;"
        "xchg %0, %1;"
        "testl %1, %1;"
        "jnz enter;"

        :"=m"(*tas), "=a"(ret)
        :"a"(1), "m"(*tas));

    return ret;
}

int unlock(int* tas) {
    int ret;
    // Inline assembly that sets the value of ret to the current value of tas,
    // and sets the value of tas to 0.
    asm("xchg %0, %1;"

        :"=m"(*tas), "=a"(ret)
        :"a"(0), "m"(*tas));

    return ret;
}