#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    //Asks for text input

    string text = get_string("Text: ");
    //Defines function that counts number of letters
    int letters = count_letters(text);
    //Defines function that counts number of words
    printf("%i\n", letters);
    int words = count_words(text);
    //Defines function that counts number of sentences
    printf("%i\n", words);
    int sentences = count_sentences(text);
    //Defines L as average number of letters per 100 words
    double L = ((1.0 * letters) / (1.0 * words)) * 100;
    //Defines S as average number of sentences per 100 words
    printf("%f\n", L);
    double S = ((1.0 * sentences) / (1.0 * words)) * 100;
    printf("%f\n", S);
    //Place variables in
    double index = (0.0588 * L) - (0.296 * S) - 15.8;
    //Round score to nearest whole number
    printf("%f\n", index);
    int level = round(index);
    //If reading level is below grade 1
    if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    //If reading level is at least grade 1 and less than grade 16
    if (level >= 1 && level < 16)
    {
        printf("Grade %i\n", level);
    }
    //If reading level is above grade 16
    if (level > 16)
    {
        printf("Grade 16+\n");
    }
}

//Count letters in a string of text
int count_letters(string text)
{
    //Calculate length of the text
    int length = strlen(text);
    //Create a variable called letters to keep track of how many letters are in string and set at 0
    int letters = 0;
    //For function where you loop through string checking if each character is a letter
    for (int i = 0; i < length; i++)
    {
        //Looks at the character in position i of the string (represented as an array of characters)
        char c = text[i];
        //If it is alphabetical, add 1
        if (isalpha(c))
        {
            letters++;
        }
    }
    return (letters);
}

//Count words in a string of text
int count_words(string text)
{
    //Calculate length of the text
    int length = strlen(text);
    //Create a variable called words to keep track of how many words are in string and set at 1 since there are n-1 spaces between n words
    int words = 1;
    //For function where you loop through string checking how many spaces there are and adding to word count
    for (int i = 0; i < length; i++)
    {
        //Looks at the character in position i of the string (represented as an array of characters)
        char c = text[i];
        //If it is a space, add 1 because there's another word
        if (isspace(c))
        {
            words++;
        }
    }
    return (words);
}

//Count sentences in a string of text
int count_sentences(string text)
{
    //Calculate length of the text
    int length = strlen(text);
    //Set number of sentences at 0
    int sentences = 0;
    //For function where you loop through string checking for end-stopped punctuation and adding to number of sentences
    for (int i = 0; i < length; i++)
    {
        //Looks at the character in position i of the string (represented as an array of characters)
        char c = text[i];
        //If the character is a period, add 1 to sentences
        if (c == '.')
        {
            sentences++;
        }
        //If the character is a question mark, add 1 to sentences
        if (c == '?')
        {
            sentences++;
        }
        //If the character is an exclamation mark, add 1 to sentences
        if (c == '!')
        {
            sentences++;
        }
    }
    printf("%i\n", sentences);
    return (sentences);
}