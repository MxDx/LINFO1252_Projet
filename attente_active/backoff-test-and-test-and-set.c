#include <unistd.h>

int lock(int *tatas, int *vmax) {
    int ret;
    // Inline assembly that sets the value of ret to the current value of tatas,
    // and sets the value of tatas to 1.
    int i=2;
    while (*tatas == 1){
        if(i^2 >*vmax){
            usleep(*vmax);

        }
        else{
            usleep(i^2);
            i++;
        }
    }
    
    asm(
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