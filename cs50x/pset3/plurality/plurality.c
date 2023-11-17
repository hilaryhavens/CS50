#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    //Count the number of votes indexing at 0 and running through them
    for (int i = 0; i < candidate_count; i++)
    {
        //Compare input with the candidate names, and if they are the same
        if (strcmp(candidates[i].name, name) == 0)
        {
            //Add to the specific candidate's vote total
            candidates[i].votes++;
            return true;
        }
    }
    //If the input is not a candidate name, return a false value
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    //Determine the highest vote total
    int vote_winner = 0;
    //Cycle through all the votes
    for (int i = 0; i < candidate_count; i++)
    {
        //Compare a candidate vote count with the current highest total.  If it is greater, set it as the new vote winner.
        if (candidates[i].votes >= vote_winner)
        {
            vote_winner = candidates[i].votes;
        }
    }

    //Print winner once highest vote total is set.
    //Cycle through all the votes
    for (int j = 0; j < candidate_count; j++)
    {
        //If a candidate vote count is the same as the maximum vote count
        if (candidates[j].votes == vote_winner)
        {
            //Print that candidate's name
            printf("%s\n", candidates[j].name);
        }
    }
    return;
}