#include <bits/stdc++.h>

using namespace std;

int checkPresent(string a, string b) // Checks for the presence of a in b
{
    int len1 = a.length();
    int len2 = b.length();

    for (int i = 0; i <= len2 - len1; i++) {
        int j;
        for (j = 0; j < len1; j++)
            if (b[i + j] != a[j])
                break; 
        if (j == len1)
            return i;
    }
 
    return -1;
}
 

int main() {
    printf("Welcome to the game of bug bounty hunting castle\n");
    printf("Let's see if you can get the secret hidden within.\nYou are provided with a few bounty points intially.\nFor proving your worth, you need to fight some monsters on your way and for that you would have to invest your bounty points.\n");
    printf("You would be requiring a certain number of bounty points in the end to win the right to know the secret about the castle!\n");
    printf("Best of luck for your pursuit!\n");
    int connection = 1;
    int bounty_points = 1000;
    while (connection) {
        printf ("\n[1] Check your bounty points");
        printf ("\n[2] Move ahead");
        printf ("\n[3] Arghhh, I can't bear this no more! Take me out");
        int option;
        printf ("\n Enter what you would like to do? \n");
        cin >> option;
        switch (option) {
            case 1:
                printf ("\n Current bounty points = %d \n", bounty_points);
                break;
            case 2:
                printf ("\n Welcome to the next level \n");
                printf ("[1] Fight Monsters\n");
                printf ("[2] Know the secret\n");
                printf ("\n What would you like to do next? \n");
                int choice;
                cin >> choice;
                if (choice == 1) {
                    printf ("Each fight with monster will cause you 1000 points, how many are you willing to fight with?\n");
                    int num = 0;
                    cin >> num;
                    if (num > 0) // Not gonna be that easy :P 
                    {
                        int tot = 1000*num;
                        printf ("\n Total bounty points going to be used are: %d\n", tot);
                        if (tot <= bounty_points) 
                        {
                            bounty_points -= tot;
                            printf ("Total bounty points after fight are: %d\n", bounty_points);
                        }
                        else 
                        {
                            printf ("Not enough points left\n");
                        }
                    }
                    else {
                        printf ("Please enter a valid input!\n");
                    }
                }
                else if (choice == 2) {
                    printf ("It will require 100000000 bounty points to know the secret\n");
                    printf ("Type 1 to know it\n");
                    int reply;
                    cin >> reply;
                    if (reply == 1) {
                        if (bounty_points > 100000000) {
                            printf ("Great you were so brave to fight those many monsters!\n");
                            printf ("You meet a sage lying at the foot of the caves waiting for someone to come one day and get the secret. He guides you to the tresure!\n");
                            printf ("The sage goes on to say, 'Unfortunately the secret roll is present somewhere in the cave and I am having trouble traversing the caves.'\n");
                            printf ("He adds, 'Seems like the ruler only wants to you to see what's inside the cave, but I know that there is a gate out there which might lead you to treasure named secret.txt.' Can you traverse pass that door somehow?\n");
                            // Executing the required commands
                            char cmd[100];
                            cin.ignore();
                            cin.getline(cmd, sizeof(cmd));
                            char notallowed1[3] = "cd";
                            char notallowed2[4] = "cat"; 
                            char notallowed3[3] = "ls";
                            if (checkPresent(notallowed1, cmd) == -1 && checkPresent(notallowed2, cmd) == -1 && checkPresent(notallowed3, cmd) == -1) 
                            {
                                FILE *f;
                                char line[100];
                                f = popen(cmd , "r");
                                if (f == ((FILE *)NULL))
                                {
                                    perror("poeb");
        
                                }
                                while (fgets(line, sizeof line, f)) {
                                    printf ("%s", line);
                                }
                            }
                            else {
                                printf("Not that easy! :P");
                            }
                            connection = 0;
                        }
                        else {
                            printf ("Not enough points, come back later!");
                        }
                    }
                }
                break;
            default: 
                connection = 0;
        }  
    }
    return 0;
}
