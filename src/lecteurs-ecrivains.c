#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/*
On favorise les writer ici
*/

pthread_mutex_t m_rcount;
pthread_mutex_t m_wcount;

sem_t wsem; // accès à la wsem
sem_t rsem; // bloque les lecteurs

int readcount=0; // nombre de readers
int writecount=0; // nombre de writers

int global_count=0;

void* writer(void* param) {
    int* times_to_run = (int*) param;
    int counter = 0;
    while(counter < *times_to_run) {
        pthread_mutex_lock(&m_wcount);
        writecount++;
        if(writecount == 1) {
            // Si première écrivain --> On bloque les prochains reader d'arriver
            sem_wait(&rsem); 
        }
        pthread_mutex_unlock(&m_wcount);        

        sem_wait(&wsem); // On attend maintenant que tous les reader on finis

        global_count++;
        for(int i=0;i<10000;i++){
            //Sisimulation
        }

        sem_post(&wsem);

        pthread_mutex_lock(&m_wcount);
        writecount--;
        if(writecount == 0) {
            sem_post(&rsem);
        } 
        pthread_mutex_unlock(&m_wcount);
        counter++;
    }
    return NULL;
}


void* reader(void* param) {
    int* times_to_run = (int*) param;
    int counter = 0;
    while(counter < *times_to_run){
        sem_wait(&rsem); // Permet de bloquer les reader avec le writer
        pthread_mutex_lock(&m_rcount);
        // section critique
        readcount++;
        if (readcount==1) { // arrivée du premier reader
            sem_wait(&wsem);
        }
        pthread_mutex_unlock(&m_rcount);
        sem_post(&rsem); // Libère la sem quand il a finis

        for(int i=0;i<10000;i++){
            //sisimulation
        } 

        pthread_mutex_lock(&m_rcount);
        // section critique
        readcount--;
        if(readcount==0) { // départ du dernier reader
            sem_post(&wsem);
        }
        pthread_mutex_unlock(&m_rcount);
        counter++;
    }
    return NULL;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Number of reader and writer not given\n");
        return 1;
    }

    int* nb_thread_reader = (int*) malloc(sizeof(int));
    int* nb_thread_writer = (int*) malloc(sizeof(int));

    *nb_thread_reader = atoi(argv[1]);
    *nb_thread_writer = atoi(argv[2]);

    int times_to_run_read = 2560/ *nb_thread_reader;
    int reste_read = 2560% *nb_thread_reader + times_to_run_read;

    int times_to_run_writer = 640/ *nb_thread_writer;
    int reste_write = 640% *nb_thread_writer + times_to_run_writer;

    sem_init(&wsem, 0, 1);
    sem_init(&rsem, 0, 1);

    pthread_t threads_reader[*nb_thread_reader];
    pthread_t threads_writer[*nb_thread_writer];
    for (int i=0; i<*nb_thread_reader-1; i++) {
        pthread_create(&threads_reader[i], NULL, &reader, (void*) &times_to_run_read );
    }
    pthread_create(&threads_reader[*nb_thread_reader-1], NULL, &reader, (void*) &(reste_read));

    for (int i=0; i<*nb_thread_writer-1; i++) {
        pthread_create(&threads_writer[i], NULL, &writer,(void*) &times_to_run_writer );
    }
    pthread_create(&threads_writer[*nb_thread_writer-1], NULL, &writer, (void*) &(reste_write));

    for (int i=0; i<*nb_thread_reader; i++) {
        pthread_join(threads_reader[i], NULL);
    }

    for (int i=0; i<*nb_thread_writer; i++) {
        pthread_join(threads_writer[i], NULL);
    }

    return 0;
}