//Implements a list of numbers as a binary search tree

#include <stdio.h>
#include <stdlib.h>

//represents a node
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

//Prototypes for functions that allow freeing and printing tree
void free_tree(node *root);
void print_tree(node *root);

int main(void)
{
    //Tree of size 0
    node *tree = NULL;

    //Add number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    //initializing node to contain 2 and left and right children, and then tree
    n->number = 2;
    n->left = NULL;
    n->right = NULL;
    tree = n;

    //Add number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        //Free memory
        return 1;
    }
    //Initialize number to 1 and new children, and then initialize tree's left child to be n
    n->number = 1;
    n->left = NULL;
    n->right = NULL;
    tree->left = n;

    //Add number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 3;
    n->left = NULL;
    n->right = NULL;
    tree->right = n;

    //Print tree
    print_tree(tree);

    //Free tree
    free_tree(tree);
}

void free_tree (node *root)
{
    if (root == NULL)
    {
        return;
    }
    free_tree (root->left);
    free_tree(root->right);
    free(root);
}

//Takes a pointer to root as argument
void print_tree (node *root)
{
    if (root == NULL)
    {
        return;
    }
    //Recursion example (order doesn't matter)
    print_tree(root->left);
    printf("%i\n", root->number);
    print_tree(root->right);
}