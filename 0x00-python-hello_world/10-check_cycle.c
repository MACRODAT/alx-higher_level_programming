#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - is there a cycle ?
 * @list: list
 *
 * Return: 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *nxt;
	listint_t *aft;

	if (list == NULL || list->next == NULL)
		return (0);

	nxt = list->next;
	aft = list->next->next;

	while (nxt && aft && aft->next)
	{
		if (nxt == aft)
			return (1);

		nxt = nxt->next;
		aft = aft->next->next;
	}

	return (0);
}
