//Name: Stefanie Shidoosh
//UID: 804794484

#include <stdlib.h>
#include <stdio.h>

int frobcmp (char const*a, char const*b)
{
    while((*a != ' ') && (*b != ' '))
    {
        if ((*a^42) < (*b^42))
            return -1;
        if ((*a^42) > (*b^42))
            return 1;
        a++;
        b++;
        
    }
    if ((*a != ' ') && (*b == ' '))
        return 1;
    if ((*a == ' ') && (*b != ' '))
        return -1;
    return 0;
}

int compare(const void* x, const void*y)
{
    char const*a = *(char const**)x;
    char const*b = *(char const**)y;
    return frobcmp(a, b);
}


void error()
{
    if(ferror(stdin))
    {
        fprintf(stderr, "File could not be read");
        exit(1);
    }
}

int main(void)
{
    
    int allIt=0;
    int letterIt=0;
    
    char** all;
    char* curr;
    
    all=(char**)malloc(sizeof(char*));
    curr = (char*)malloc(sizeof(char));
    
    int currChar = getchar();
    error();
    
    int loop = 0;
    int lastChar=0;
    
    while(loop == 0)
    {
        if(lastChar == 1)
        {
            curr[letterIt] = ' ';
            loop = 1;
        }
        else
            curr[letterIt] = currChar;
    
        char *temp = realloc(curr, (letterIt+2)*sizeof(char));
        if(temp != NULL)
        {
            letterIt++;
            curr = temp;
        }
        else
        {
            fprintf(stderr, "Memory allocation fail");
            free(curr);
            exit(1);
        }
        if(currChar == ' ' || lastChar == 1)
        {
            all[allIt] = curr;
            char **allTemp = realloc (all, (allIt+2)*sizeof(char*));
            if(allTemp != NULL)
            {
                all = allTemp;
                allIt++;
                curr = NULL;
                curr = (char*)malloc(sizeof(char));
                letterIt=0;
            }
            else
            {
                fprintf(stderr, "Memory allocation fail");
                free(all);
                exit(1);
            }
        }
        int nextChar = getchar();
        error();
        if(nextChar == EOF)
            lastChar = 1;
        
        currChar = nextChar;
    }
    qsort(all, allIt, sizeof(char*), compare);
    int i;
    int j;
    for (i = 0; i< allIt; i++)
    {
        for(j = 0;;j++)
        {
            if(putchar(all[i][j]) == EOF)
            {
                fprintf(stderr, "Characters could not be printed");
                exit(1);
            }
            if(all[i][j] == ' ')
                break;
        }
    }
    for(i = 0; i < letterIt; i++)
    {
        free(all[i]);
    }
    free(curr);
    exit(0);
}


