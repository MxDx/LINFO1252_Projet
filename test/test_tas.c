#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <pthread.h>
#include "../headers/test-and-set.h"

int tas = 0;
int* nb_thread;

void* thread_func(void* arg) {
    int* nb = (int*) arg;

    for (int i = 0; i < *nb; i++) {
        lock(&tas);
        for (int j = 0; j < 10000; j++);
        unlock(&tas);
    }

    return NULL;
}

int main(int argc, char* argv[]) {
    
    if (argc != 2) {
        printf("Number of threads not given\n");
        return 1;
    }

    nb_thread = (int *)malloc(sizeof(int));
    *nb_thread = atoi(argv[1]);

    pthread_t* threads = (pthread_t *)malloc(*nb_thread * sizeof(pthread_t));

    int times_to_run = 6400 / *nb_thread;
    int times_to_run_last = times_to_run + 6400 % *nb_thread;

    for (int i = 0; i < *nb_thread-1; i++) {
        pthread_create(&threads[i], NULL, thread_func, (void *) &times_to_run);
    }
    pthread_create(&threads[*nb_thread-1], NULL, thread_func, (void *) &times_to_run_last);

    for (int i = 0; i < *nb_thread; i++) {
        pthread_join(threads[i], NULL);
    }

    free(threads);
    free(nb_thread);

    return 0;
}