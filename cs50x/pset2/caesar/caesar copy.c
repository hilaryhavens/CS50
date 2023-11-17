#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int key;
bool only_digits(string s);
char rotate(char c, int n);

//Get key
int main(int argc, string argv[])
{
    //If the user put in 1 input
    if (argc == 2)
    //Calculate length of the text
    {
        string input = argv[1];
        int length = strlen(input);
        //For function where you loop through string checking if every character is a digit
        for (int i = 0; i < length; i++)
        {
            //Looks at the character in position i in argv[1]
            char c = input[i];
            //If it is a digit
            if (isdigit(c++))
            {
            //Convert string input to integer
            key = atoi(input);
            return key;
            }
            else
            {
                printf("Usage: ./caesar key\n");
            }
        }
    }
    //If the user didn't put in one input or didn't put in digits
    else
    {
        printf("Usage: ./caesar key\n");
    }

    //Get plaintext
    string plaintext = get_string("plaintext: ");
    //Find the length of plaintext
    int length = strlen(plaintext);
    //For loop running through every character in plaintext
    for (int i = 0; i < length; i++)
    {
        //For every character in the length of plaintext
        char c = plaintext[i];
        //If the character is alphabetical
        if isalpha(c)
        {
            //If it is uppercase
            if isupper(c)
            {
                c = (c + key) % 26;
                printf("%c", c);
            }
            //If it is lowercase
            else if islower(c)
            {
                c = (c + key) % 26;
                printf("%c", c);
            }
        }
        //If the character is not alphabetical
        else
        {
            //Print as is
            printf("%c",c);
        }

    }

    //encipher with cases preserved and non-alphabetical characters the same


    //print ciphertext

}