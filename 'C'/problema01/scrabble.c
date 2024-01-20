#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
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

    // Print the winner based on the scores
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 == score2)
    {
        printf("Empate!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}

int compute_score(string word)
{
    int score = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
            if (word[i] < 'a' || word[i] > 'z')
            {
                int index;
                if (isupper(word[i]))
                {
                    index = word[i] - 'A';
                }
                else
                {
                    index = word[i] - 'a';
                }

                score += POINTS[index];
            }
        }

    return score;
}
