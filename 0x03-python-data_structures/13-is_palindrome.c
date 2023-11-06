#include "lists.h"

/**
 * is_palindrome - is palin
 * @head: linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *lst, *tmp, *t;
	int _len = 1, i = 0;

	if (!head || !*head)
		return (1);
	lst = *head;
	while (lst && lst->next)
	{
		_len++;
		lst = lst->next;
	}
	i = (1 + _len) / 2;
	lst = *head;
	while (i--)
		lst = lst->next;
	tmp = 0;
	while (lst)
	{
		t = lst->next;
		lst->next = tmp;
		tmp = lst;
		lst = t;
	}
	lst = tmp;
	tmp = *head;
	while (tmp && lst)
	{
		if (tmp->n != lst->n)
			return (0);
		tmp = tmp->next;
		lst = lst->next;
	}
	return (1);
}
