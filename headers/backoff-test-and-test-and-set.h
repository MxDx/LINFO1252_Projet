#ifndef TEST_AND_TEST_AND_SET
#define TEST_AND_TEST_AND_SET

int lock(int *tas, int* vmax); 

int unlock(int* tas);

#endif