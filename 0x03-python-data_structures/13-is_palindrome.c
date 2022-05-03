#include "lists.h"

/**
 * reverse - reverses linked list
 * @nodo_medio: ptr to a center to the linked list
 * Return: return head of a reversed list
 */
void reverse(listint_t **nodo_medio)
{
	listint_t *prev = NULL;
	listint_t *current = *nodo_medio;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*nodo_medio = prev;
}

/**
 *is_palindrome - function comprobe if a linked list is palindrome or not
 *@head: pointer to a point to first node
 *Return: 1 if is palindrome or 0 is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_of_slow_ptr = *head;
	listint_t *midnode = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	else
	{
        	while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
            		fast_ptr = fast_ptr->next->next;

			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}
		if (fast_ptr != NULL)
		{
			midnode = slow_ptr;
			slow_ptr = slow_ptr->next;
		
        	}

		second_half = slow_ptr;
                prev_of_slow_ptr->next = NULL;
                reverse(&second_half);

		if (midnode != NULL)
		{
			prev_of_slow_ptr->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow_ptr->next = second_half;
		return (1);
	}
	return (0);
}
