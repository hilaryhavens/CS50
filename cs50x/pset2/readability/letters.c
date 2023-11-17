#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int letters;

int main(void)
{
    string text = get_string("Text: ");
    int length = strlen(text);
    //create a variable called letters to keep track of how many letters are in string and set at 0
    letters = 0;
    //For function where you loop through string checking if each character is a letter
    //isuppercase and islowercase - add 1, otherwise add 0
    for (int i = 0; i < length; i++)
    {
        char c = text[i];
        //If it is alphabetical, add 1
        if (isalpha(c))
        {
            letters++;
        }
    }
    printf("%i\n", letters);
}