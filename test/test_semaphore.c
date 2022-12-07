#include <stdlib.h>
#include "../headers/semaphore.h"

int main() {
    sem_s* sem = (sem_s*) malloc(sizeof(sem_s));
    sem_init(sem, 2);
    sem_wait(sem);
    sem_wait(sem);

    sem_post(sem);
    sem_post(sem);
    return 0;
}