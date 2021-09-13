#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	unsigned int size = 0, i = 0;
	int T[99999];

	if (head == NULL) 
		return (0);

	if (*head == NULL) 
		return (1);

	while (tmp) 
	{
		tmp = tmp->next;
		size += 1;
	}
	if (size == 1) 
		return (1);

	tmp = *head;
	while (tmp) 
	{
		T[i++] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i <= (size/2); i++)
	{
		if (T[i] != T[size - i - 1])
			return (0);
	}
	return (1);
}
