#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stdbool.h>

/**
 * reverse - function to reverse array
 * @head: head pointer parameter
 * Return: Void
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}


/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer parameter
 * Return: True or False
 */

int is_palindrome(listint_t **head)
{
	listint_t *s_ptr = *head;
	listint_t *f_ptr = *head;
	listint_t *prev_s_ptr = *head;
	listint_t *middile_ptr = NULL;
	listint_t *sec_half = NULL;
	listint_t *i = NULL;
	listint_t *j = NULL;
	bool is_palindrome = true;

	if (*head != NULL && *head->next != NULL)
	{
		while (f_ptr != NULL && f_ptr->next != NULL)
		{
			f_ptr = f_ptr->next->next;
			prev_s_ptr = s_ptr;
			s_ptr = s_ptr->next;
		}
		if (f_ptr != NULL)
		{
			middle_ptr = s_ptr;
			s_ptr = s_ptr->next;
		}
		sec_half = s_ptr;
		prev_s_ptr = NULL;
		reverse(&sec_half);

		while (i != NULL && j != NULL)
		{
			if (i->data != j->data)
			{
				is_palindrome = false;
				break;
			}
			i = i->next;
			j = j->next;
		}
		reverse(&sec_half);
		prev_s_ptr->next = middle_ptr;
		if (middle_ptr != NULL)
		{
			middle_ptr->next = sec_half;
		}
		else
		{
			*head = sec_half;
		}
	}
	return (is_palindrome ? 1 : 0);
}
