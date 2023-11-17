#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char letter, int n);

int main(int argc, string argv[])
{
    //If the user put in 1 input that is only digits
    if (argc == 2 && (only_digits(argv[1])))
    {
        //Convert key to an integer
        int key = atoi(argv[1]);
        //Ask user for plaintext
        string ptext = get_string("plaintext: ");
        //Print ciphertext through the following for loop
        printf("ciphertext: ");
        //For loop running through every character in plaintext bounded by length
        for (int i = 0; i < strlen(ptext); i++)
        {
            //Print each character by rotating the original character by the key
            printf("%c", (rotate(ptext[i], key)));
        }
        //Line break
        printf("\n");
        return 0;
    }
    //If the user didn't put in one input or didn't put in digits
    else
    {
        //Print error message and exit program
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

//Function to check to see if input is only digits
bool only_digits(string s)
{
    //For function where you loop through string checking if every character is a digit
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        //If the function comes across a non-digit, return false value
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    //Otherwise, confirmation that input is digits.
    return true;
}

//Function to rotate characters by key
char rotate(char c, int n)
{
    //If the character is alphabetical
    if isalpha(c)
    {
        //If it is uppercase
        if isupper(c)
        {
            int d = (((int) c - 64 + n) % 26) + 64;
            return d;
        }
        //If it is lowercase
        if islower(c)
        {
            int d = (((int) c - 96 + n) % 26) + 96;
            return d;
        }
        //If the character is not alphabetical
    }
    else
    {
        //Print as is
        return c;
    }
    return 0;
}