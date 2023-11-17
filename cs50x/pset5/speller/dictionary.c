// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
//Previous 26
const unsigned int N = 4050;

// Hash table
node *table[N];

//Counter for number of words in dictionary set to 0;
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //Hash word to obtain a hash value using the hash function
    int index = hash(word);
    //Create a cursor variable to scan through linked list at that index
    node *cursor = table[index];
    //Go through list one word at a time using strcasecmp until NULL is reached
    while (cursor != NULL)
    {
        //Use strcomp to compare
        if (strcasecmp(word, cursor->word) == 0)
        {
            //ONCE you find the word, answer true
            return true;
        }
        cursor = cursor->next;
    }
    //If word not there, cursor will become null and function will return false
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    //Sum of ASCII values of letters?  Run loop?

    //Find length of word
    int n = strlen(word);
    //initialize value variable
    int sum = 0;
    //Iterate for each character along the length of the word
    for (int i = 0; i < n; i++)
    {
        int value = (toupper(word[i]) - 'A');
        sum = value++;
    }
    return sum;
    //OLD hash function
    //return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //Open dictionary file
    FILE *file = fopen(dictionary, "r");
    //Check if return value is NULL
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }

    char word[LENGTH + 1];

    //word = character array inside memory where you can access individual characters of word after you have read it from file
    while (fscanf(file, "%s", word) != EOF)
    {
        //Create a new node for each word
        //Allocate memory for new node (Address of node inside of n)
        node *n = malloc(sizeof(node));
        //If return value of malloc is NULL (not enough memory), load function should return false
        if (n == NULL)
        {
            printf("Not enough memory.\n");
            return false;
        }

        //Put data into that node
        strcpy(n->word, word);

        //Hash word to obtain a hash value - index into hash table to determine which of linked lists to use
        int index = hash(word);

        //Insert node into hash table at that location
        //If word not there, add a new node to linked list
        if (table[index] == NULL)
        {
            table[index] = n;
            //Set it as the head
            n->next = NULL;
        }
        //If the node is already there, indicate location
        else
        {
            //Set pointer of new node to be first element, and then set pointer of head to be new (now first) node
            n->next = table[index];
            //Add a word to number of words in dictionary
            table[index] = n;
        }
        word_count++;
    }
    fclose(file);
    return word_count;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //Call free on any memory allocated using malloc
    //Iterate over individual linked lists and calling free over each of them
    for (int i = 0; i < N; i++)
    {
        //Define variables
        node *cursor = table[i];
        //Initialize variable tmp
        node *tmp = NULL;
        //Run loop until end of list
        while (cursor != NULL)
        {
            //Set tmp equal to cursor
            tmp = cursor;
            //move cursor to next node so you don't lose the list
            cursor = cursor->next;
            //free the memory from previous node
            free(tmp);
        }
    }
    return true;
}
