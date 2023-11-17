#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string ptext = get_string("plaintext: ");
    //Find the length of plaintext
    int n = strlen(ptext);
    //For loop running through every character in plaintext
    for (int i = 0; i < n; i++)
    {
        //For every character in the length of plaintext
        char c = ptext[i];
        if isalpha(c)
        {
            //If it is uppercase
            if isupper(c)
            {
                int d = (((int) c - 64 + 2) % 26) + 64;
                printf("%c", d);
            }
            //If it is lowercase
            if islower(c)
            {
                int d = (((int) c - 96 + 2) % 26) + 96;
                printf("%c", d);
            }
        }
        //If the character is not alphabetical
        else
        {
            //Print as is
            printf("%c", c);
        }
    }
}