#include "lists.h"

/**
*insert_node - add a node in the correct place
*@head: pointer to point a list
*@number: number of each node (id)
*Return: point to a list with the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *to_add, *aux = *head, *node_anterior = NULL;

	to_add = malloc(sizeof(listint_t));
	if (to_add == NULL)
		return (NULL);
	/*no hay ningun nodo y metemos el nuestro*/
	to_add->n = number;
	if (*head == NULL)
	{
		*head = to_add;
		to_add->next = NULL;
	}
	else
	{
		while (number > aux->n && aux->next != NULL)
		{
			/*dejamos un puntero al nodo anterior*/
			node_anterior = aux;
			aux = aux->next;
			/*con el loop encontramos la pos donde iría*/
		}
		/*porque salió del while*/
		if (number > aux->n)
		{
			aux->next = to_add;
			to_add->next = NULL;
		}
		else if (node_anterior == NULL)
		{
			to_add->next = *head;
			*head = to_add;
		}
		else
		{
			to_add->next = aux;
			node_anterior->next = to_add;
		}
	}
	return (*head);
}
