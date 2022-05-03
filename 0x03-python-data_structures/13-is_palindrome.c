#include "lists.h"

/**
 * reverse - reverses linked list
 * @nodo_medio: ptr to a center to the linked list
 * Return: return head of a reversed list
 */
listint_t *reverse(listint_t *nodo_medio)
{
	listint_t *prev = NULL;
	listint_t *curr = nodo_medio;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

/**
 *is_palindrome - function comprobe if a linked list is palindrome or not
 *@head: pointer to a point to first node
 *Return: 1 if is palindrome or 0 is not
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	return (0);
}
