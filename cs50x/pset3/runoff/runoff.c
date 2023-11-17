#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid - voter (which voter), rank (which rank), and name of the candidate
bool vote(int voter, int rank, string name)
{
    //Compare with every entry in the candidate count
    for (int i = 0; i < candidate_count; i++)
    {
        //Compare input with the candidate names, and if they are the same
        if (strcmp(candidates[i].name, name) == 0)
        {
            //If candidate found, update preferences so that they are the voter's rank preference and return true
            preferences[voter][rank] = i;
            return true;
        }
    }
    //If the input is not a candidate name, return a false value
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    //Run through each voter's votes
    for (int i = 0; i < voter_count; i++)
    {
        int j = 0;
        while (candidates[preferences[i][j]].eliminated == true)
        {
            j++;
        }
        //Increase vote total to candidate at location preferences[i][j] if candidate not eliminated
        candidates[preferences[i][j]].votes++;
    }
    return;
}

//Print the winner of the election, if there is one
bool print_winner(void)
{
    //Calculate number of votes needed to win the election
    float win = (voter_count * 0.5);
    //Run through total number of candidates to find winner
    for (int i = 0; i < voter_count; i++)
    {
        //Check if any candidate has more than 50%
        if (candidates[i].votes > win)
        {
            //Print out name and return true
            printf("%s\n", candidates[i].name);
            return true;
        }
    }
    //If no candidate has more than half of the vote
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    //Initialize min
    int min;
    //Run through the number of candidates in the election
    for (int i = 0; i < candidate_count; i++)
    {
        //Exclude eliminated candidates
        if (!candidates[i].eliminated)
        {
            //Set minimum value to unelimated candidate i
            min = candidates[i].votes;
            //If this minimum is greater than other candidate i
            if (candidates[i].votes <= min)
            {
                //Find and assign new minimum number of votes to n
                min = candidates[i].votes;
            }
        }
    }
    return min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    //Run through the number of candidates in the election
    for (int i = 0; i < candidate_count; i++)
    {
        //Exclude eliminated candidates and if all of the votes left are the same
        if (!candidates[i].eliminated && min != candidates[i].votes)
        {
            //Indicate there is no tie
            return false;
        }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    //Run through the number of candidates in the election
    for (int i = 0; i < candidate_count; i++)
    {
        //Exclude already eliminated candidates and eliminate anyone still in the race with min number of votes
        if (candidates[i].votes == min)
        {
            //Should update specific candidate struct and change bool value of eliminated
            candidates[i].eliminated = true;
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}