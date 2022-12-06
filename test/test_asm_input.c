#include <stdio.h>

int main(void){
    int x = 10, y, z;
  
    asm ("movl %1, %%eax;"
       "movl %%eax, %0;"
    :"=r"(y)  /* y is output operand */
    :"r"(x)   /* x is input operand */
    :"%eax"); /* %eax is clobbered register */

    asm("movl %0, %%eax;"
    : "=r"(z)
    : "r"(y+4));
    printf("z = %d\n", z);

    printf("x = %d, y = %d \n", x, y);

    return 0;
}