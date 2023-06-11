#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stdbool.h>

/**
 * reverse - function to reverse array
 * @head: head pointer parameter
 * Return: Void
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer parameter
 * Return: True or False
 */


int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev_slow->next = NULL;
		second_half = reverse(second_half);

		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}

		second_half = reverse(second_half);
		if (mid != NULL)
		{
			prev_slow->next = mid;
			mid->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}
	return (is_palindrome);
}
