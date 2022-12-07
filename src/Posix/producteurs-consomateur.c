#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <semaphore.h>
#include "../../headers/stack.h"

sem_t* buffer_cons; // Semaphore pour les consommateurs
sem_t* buffer_prod; // Semaphore pour les producteurs

//Utilisation d'une stack pour implémenter le buffer

stack_t* stack;

pthread_mutex_t stack_mutex; // Mutex pour la stack


void* productor(void* args) {
    int counter = 0; // Compteur pour savoir quand arrêter le thread car cchaque thread fait 8192/nb_thread opérations
    int* times_to_run = (int*) args;
    while (counter < *times_to_run) {
        sem_wait(buffer_prod);
        pthread_mutex_lock(&stack_mutex);
        push(stack, (void*) 1);
        pthread_mutex_unlock(&stack_mutex);
        for (int i = 0; i < 100000; i++) {
            // pass
        }
        sem_post(buffer_cons);

        counter++;
    }
    return NULL;
}

void* consumer(void* args) {
    int counter = 0; // Compteur pour savoir quand arrêter le thread car cchaque thread fait 8192/nb_thread opérations
    int* times_to_run = (int*) args;
    int* res = (int*) malloc(sizeof(int));
    while (counter < *times_to_run) {
        sem_wait(buffer_cons);

        pthread_mutex_lock(&stack_mutex);
        int* res = (int*) pop(stack);
        pthread_mutex_unlock(&stack_mutex);

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
    pthread_mutex_init(&stack_mutex, NULL);
    buffer_prod = (sem_t*) malloc(sizeof(sem_t));
    buffer_cons = (sem_t*) malloc(sizeof(sem_t)); 

    *nb_thread_cons = atoi(argv[1]);
    *nb_thread_prod = atoi(argv[2]);

    int times_to_run_prod = 8192/ *nb_thread_prod;
    int reste_prod = 8192% *nb_thread_prod + times_to_run_prod;

    int times_to_run_cons = 8192/ *nb_thread_cons;
    int reste_cons = 8192% *nb_thread_cons + times_to_run_cons;

    sem_init(buffer_prod, 0 ,8);
    sem_init(buffer_cons, 0, 0);

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