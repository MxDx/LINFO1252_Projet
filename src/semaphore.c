


// Semaphore structure
typedef struct sem_s {
    int tatas;
    int counter;
} sem_s;

// Initialize semaphore
void sem_init(sem_s *sem, unsigned int val) {
    sem->tatas = 0;
    sem->counter = val;
}

void sem_wait(sem_s *sem) {
    while((sem->counter!=0) && sem->tatas!=1);
    lock(sem->tatas);
    sem->counter--;
    unlock(sem->tatas);
}
void sem_post(sem_s *sem){
    lock(sem->tatas);
    sem->counter++;
    unlock(sem->tatas);
}