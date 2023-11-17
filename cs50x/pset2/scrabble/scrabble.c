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
    else if (score1 == score2)
    {
        printf("Tie! \n");
    }

}

//Computes and return score for string
int compute_score(string word)
{
    //Calculate word length
    int length = strlen(word);
    //Set score at start to 0
    int score = 0;
    //Run through the function the number of times equal to the string length
    for (int i = 0; i < length; i++)
    {
        //If the character is a lower-case letter, assign to points array after substracing ASCII value
        if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
        //If the character is an upper-case letter, assign to points array after substracing ASCII value
        else if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
    }
    //Return total score to main function
    return (score);
}
