#ifndef SEMAPHORE_H
#define SEMAPHORE_H

#include "test-and-test-and-set.h"

typedef struct sem_s {
    int tatas;
    int counter;
} sem_s;

void sem_init(sem_s* sem, int counter);

void sem_wait(sem_s* sem);

void sem_post(sem_s* sem);

#endif // !SEMAPHORE_H