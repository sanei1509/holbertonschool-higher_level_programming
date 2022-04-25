#include "lists.h"

/**
*check_cycle - cheking if there are a cycle
*@list: pointer to a list
*Return: 0 is not a cycle or 1 if is it.
*/

int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *aux_one = list;

	/*recorro el auxiliar*/
	while (aux_one)
	{
		aux = aux->next;
		aux_one = aux_one->aux_one;
		if (aux->aux_one)
		{
			return (1);
		}
	}
	return (0);
}
