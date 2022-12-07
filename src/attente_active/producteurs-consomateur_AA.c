#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include "../../headers/semaphore.h"
#include "../../headers/stack.h"

sem_s* buffer_cons;
sem_s* buffer_prod;
stack_t* stack;

int stack_TATAS;


void* productor(void* args) {
    int counter = 0;
    int* times_to_run = (int*) args;
    while (counter < *times_to_run) {
        sem_wait(buffer_prod);
        lock(&stack_TATAS);
        push(stack, (void*) 1);
        unlock(&stack_TATAS);
        for (int i = 0; i < 100000; i++) {
            // pass
        }
        sem_post(buffer_cons);

        counter++;
    }
    return NULL;
}

void* consumer(void* args) {
    int counter = 0;
    int* times_to_run = (int*) args;
    int* res = (int*) malloc(sizeof(int));
    while (counter < *times_to_run) {
        sem_wait(buffer_cons);

        lock(&stack_TATAS);
        int* res = (int*) pop(stack);
        unlock(&stack_TATAS);

        for (int i = 0; i < 100000; i++) {
            // pass
        }
        sem_post(buffer_prod);
        counter++;
    }
    free(res);
    return NULL;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Number of productor and consumer not given\n");
        return 1;
    }

    int* nb_thread_prod = (int*) malloc(sizeof(int));
    int* nb_thread_cons = (int*) malloc(sizeof(int));

    stack = (stack_t*) malloc(sizeof(stack_t));
    stack_TATAS=0;
    buffer_prod = (sem_s*) malloc(sizeof(sem_s));
    buffer_cons = (sem_s*) malloc(sizeof(sem_s)); 

    *nb_thread_cons = atoi(argv[1]);
    *nb_thread_prod = atoi(argv[2]);

    int times_to_run_prod = 8192/ *nb_thread_prod;
    int reste_prod = 8192% *nb_thread_prod + times_to_run_prod;

    int times_to_run_cons = 8192/ *nb_thread_cons;
    int reste_cons = 8192% *nb_thread_cons + times_to_run_cons;

    sem_init(buffer_prod,8);
    sem_init(buffer_cons,0);

    pthread_t* prod = (pthread_t*) malloc(sizeof(pthread_t) * *nb_thread_prod);
    pthread_t* cons = (pthread_t*) malloc(sizeof(pthread_t) * *nb_thread_cons);

    for (int i = 0; i < *nb_thread_prod - 1; i++) {
        pthread_create(&prod[i], NULL, productor, (void*) &times_to_run_prod);
    }
    pthread_create(&prod[*nb_thread_prod - 1], NULL, productor, (void*) &reste_prod);

    for (int i = 0; i < *nb_thread_cons - 1; i++) {
        pthread_create(&cons[i], NULL, consumer, (void*) &times_to_run_cons);
    }
    pthread_create(&cons[*nb_thread_cons - 1], NULL, consumer, (void*) &reste_cons);

    for (int i = 0; i < *nb_thread_prod; i++) {
        pthread_join(prod[i], NULL);
    }

    for (int i = 0; i < *nb_thread_cons; i++) {
        pthread_join(cons[i], NULL);
    }

    free(prod);
    free(cons);
    free(stack);
    free(buffer_prod);
    free(buffer_cons);
    free(nb_thread_prod);
    free(nb_thread_cons);

    return 0;

}