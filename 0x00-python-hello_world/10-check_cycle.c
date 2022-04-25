#include "lists.h"

/**
*check_cycle - cheking if there are a cycle
*@list: pointer to a list
*Return: 0 is not a cycle or 1 if is it.
*/

int check_cycle(listint_t *list)
{
	listint_t *aux_fast = list;
	listint_t *aux_normal = list;

	if (!list)
		return (0);
	/*recorro el auxiliar*/
	while (1)
	{
		if (aux_fast->next != NULL && aux_fast->next->next != NULL)
		{
			aux_fast = aux_fast->next->next;
			aux_normal = aux_normal->next;

			if (aux_fast == aux_normal)
				return (1);
		}
		else
			return (0);
	}
}
