#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner for 3 cases
    //Player 1 has a higher scrabble score
    if (score1 > score2)
    {
        printf("Player 1 wins! \n");
    }
    //Player 2 has a higher scrabble score
    if (score2 > score1)
    {
        printf("Player 2 wins! \n");
    }
    //Tied score
    else
    {
        printf("Tie! \n");
    }

}

int compute_score(string s)
{
    // TODO: Compute and return score for string
    //Calculate word length
    int length = strlen(s);
    //Set score at start to 0
    int score = 0;
    //Add integer values of word
    for (int i = 0, n = length; i < n; i++)
    {
        if (islower(s[i]))
        {
        //Assign lower-case letters to points array after substracing ASCII value
            score = POINTS[n-97];
            printf("%i", score);
        }
        if (isupper(s[i]))
        {
       //Assign upper-case letters to points array after substracing ASCII value
            score = POINTS[n-65];
            printf("%i", score);
        }
        //Ignore non-letter characters
        else
        {
        //Assign a value of 0
            score = 0;
            printf("%i", score);
        }
        score++;
    }
    return (score);
}
