#include "lists.h"

/**
 * check_cycle - checks for cycle
 * @list: linked list
 * Return: Always 1 on success and 0 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *turtle;

	turtle = hare = list;

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (turtle == hare)
		{
			return (1);
		}
	}
	return (0);
}
