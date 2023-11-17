#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Name variable
    int n;
    do
    {
        //Ask for height input
        n = get_int("Height: ");
    }
    //Keep running height loop for integer input less than 1 or greater 8
    while (n < 1 || n > 8);
    //Add "i" rows for "i" less than "n"
    for (int i = 0; i < n; i++)
    {
        for (int k = n - i - 1; k > 0; k--)
            //Add n-k spaces for each row where k is greater than 0
        {
            printf(" ");
        }
        //Add j hashtags for each row where j is less than or equal to n
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        //Add line break
        printf("\n");
    }
}