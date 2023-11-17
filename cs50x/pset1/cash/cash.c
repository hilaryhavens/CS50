#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}


int get_cents(void)
{
    int cents;
    do
    {
        //Question requires integer input
        cents = get_int("Change owed: ");
    }
    //Keep asking cents question until value is positive integer
    while (cents < 0);
    //Return value of cents that will be used in other parts of the program
    return (cents);
}

int calculate_quarters(int cents)
{
    //Define quarters
    int quarters;
    //Calculate number of quarters in cents
    quarters = cents / 25;
    //For cases with at least 25 cents
    if (quarters > 0)
    {
        //Print number of quarters
        printf("Quarters: %i\n", quarters);
    }
    //For cases with less than 25 cents
    else
    {
        //No quarters can be used
        quarters = 0;
        //Print number of quarters which is 0
        printf("Quarters: 0\n");
    }
    //Return value of quarters to be added in total coins
    return (quarters);
}

int calculate_dimes(int cents)
{
    //Define dimes
    int dimes;
    //Calculate number of dimes in cents
    dimes = cents / 10;
    //For cases with at least 10 cents
    if (dimes > 0)
    {
        //Print number of dimes
        printf("Dimes: %i\n", dimes);
    }
    else
    {
        //No dimes can be used
        dimes = 0;
        //Print number of dimes which is 0
        printf("Dimes: 0\n");
    }
    //Return value of dimes to be added in total coins
    return (dimes);
}

int calculate_nickels(int cents)
{
    //Define nickels
    int nickels;
    //Calculate number of nickels in cents
    nickels = cents / 5;
    //For cases with at least 5 cents
    if (nickels > 0)
    {
        //Print number of nickels
        printf("Nickels: %i\n", nickels);
    }
    else
    {
        //No nickels can be used
        nickels = 0;
        //Print number of nickels which is 0
        printf("Nickels: 0\n");
    }
    //Return value of nickles to be added in total coins
    return (nickels);
}

int calculate_pennies(int cents)
{
    //Define pennies
    int pennies;
    //Calculate number of pennies in cents
    pennies = cents / 1;
    //For cases with at least 1 cent
    if (pennies > 0)
    {
        //Print number of pennies
        printf("Pennies: %i\n", pennies);
    }
    else
    {
        //No pennies can be used
        pennies = 0;
        //Print number of pennies which is 0
        printf("Pennies: 0\n");
    }
    //Return value of pennies to be added in total coins
    return (pennies);
}

