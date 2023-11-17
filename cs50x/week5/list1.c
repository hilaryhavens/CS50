#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    //Solution: initialize original array of three values
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    //Time passes

    //Ask computer for a second chunk of memory (after safety check)
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    //Then copy numbers from old list into new list
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }
    //Add new number to end of list
    tmp[3] = 4;

    free(list);

    //Remember address of new chunk of memory
    list = tmp;

    //Print those addresses out
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);
    return 0;
}