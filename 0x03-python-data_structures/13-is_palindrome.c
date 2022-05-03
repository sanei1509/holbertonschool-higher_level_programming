#include "lists.h"

node *reverse(node *head)   //reverse the string (second part)
{
	node *p , *q;
	if(head == NULL)
	return head;
	
	p = head;
	q = p->next;
	
	if(q == NULL)
	return p;
	q = reverse(q);
	p->next-

/**
 *is_palindrom - function comprobe if a linked list is palindrome or not
 *@head: pointer to a point to first node
 *Return: 1 if is palindrome or 0 is not
 */

int is_palindrome(listint_t **head)
{
	node *aux, *aux2;
	
	if (*head = NULL)
	{
		return (1);
	}

	/*split*/
        
}
