#include "lists.h"

void check_even_odd_length(node *head)
{
	node *p;
	p = start;
	while(1)
	{
		if(p == NULL)
		{
			printf("Even");
			break;
		}
		
		if(p->next == NULL)
		{
			printf("odd");
			break;
		}
		
		p = p->next->next;
	}
	
}

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
	p->next->next = p;
	p->next = NULL;
	return q;
}


/**
 *is_palindrom - function comprobe if a linked list is palindrome or not
 *@head: pointer to a point to first node
 *Return: 1 if is palindrome or 0 is not
 */

int is_palindrome(listint_t **head)
{
	node *p, *q, *first_head *second_head;
	p = *haed;
	q = *head;
	
	if (p->next = NULL)
	{
		return (1);
	}

	/*split*/
	while (1)
	{
		p = p->next->next;
		if (p == NULL)
		{
			second_head = q->next->next;
			break;
		}
		q = q->next;
	}
	q->next = NULL
}
