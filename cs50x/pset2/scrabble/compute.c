#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get input word from both players
    string word = get_string("Test word: ");
    int length = strlen(word);
    //Set score at start to 0
    int score = 0;
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    //Add integer values of word
    for (int i = 0; i < length; i++)
    {
        if (islower(word[i]))
        {
        //Assign lower-case letters to points array after substracing ASCII value
            POINTS[i] = word[i] - 'a';
            score += POINTS[i];
        }
        if (isupper(word[i]))
        {
       //Assign upper-case letters to points array after substracing ASCII value
            POINTS[i] = word[i] - 'A';
            score += POINTS[i];
        }
        //Ignore non-letter characters
        else if ('A' > word[i] || word[i] < 'z')
        {
        //Assign a value of 0
            POINTS[i] = 0;
        }
    }
    printf("Score: %i\n", score);
}
