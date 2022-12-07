#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include "../../headers/test-and-test-and-set.h"

pthread_t *phil;
int *baguette;
int *nb_phil;

void *philosophe(void *arg)
{
  int *id = (int *)arg;
  int left = *id;
  int right;
  if (*nb_phil == 1)
  {
    right = 1;
  }
  else
  {
    right = (left + 1) % *nb_phil;
  }
  int i = 0;
  while (i < 100000)
  { // Sur ingi c'est 100_000_000
    // philosophe pense
    if (left < right)
    {
      lock(&baguette[left]);
      lock(&baguette[right]);
    }
    else
    {
      lock(&baguette[right]);
      lock(&baguette[left]);
    }
    unlock(&baguette[left]);
    unlock(&baguette[right]);
    i++;
  }
  return (NULL);
}

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    printf("Number of philosophe not given\n");
    return 1;
  }
  nb_phil = (int *)malloc(sizeof(int));
  *nb_phil = atoi(argv[1]);

  phil = (pthread_t *)malloc(*nb_phil * sizeof(pthread_t));

  if (*nb_phil == 1)
  {
    baguette = (int*)malloc((*nb_phil + 1) * sizeof(int));

    for (int i = 0; i < (*nb_phil + 1); i++)
    {
      baguette[i]=0;
    }
  }
  else
  {
    baguette = (int *)malloc(*nb_phil * sizeof(int));

    for (int i = 0; i < *nb_phil; i++)
    {
      baguette[i]=0;
    }
  }

  for (int i = 0; i < *nb_phil; i++)
  {
    int id = i;
    pthread_create(&phil[i], NULL, philosophe, &id);
  }
  for (int i = 0; i < *nb_phil; i++)
  {
    pthread_join(phil[i], NULL);
  }
  free(phil);
  free(baguette);

  return 0;
}
