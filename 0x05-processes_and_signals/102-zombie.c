#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop to demo zombie processes
 * Return: 0 success
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: 0 success, or exit on failure
 */
int main(void)
{
    unsigned int i;
    size_t pid;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == 0)
        {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
    }
    infinite_while();
    return (0);
}

