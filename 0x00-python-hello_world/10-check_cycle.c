#include <stdio.h>
#include <stdlib.h>
typedef struct listint_s {
	int n;
	struct listint_s *next;
} listint_t *slow, *fast;
if (list == NULL || list->next == NULL)
	return 0;
	slow = list;
	fast = list->next;
	while (fast != NULL && fast->next != NULL){
		if (slow == fast)
			retuen 1;
		slow = slow->next;
		fast = fast->next->next;
	}
return 0;
}
int main(void) {
	listint_t *head, *second, *third;
	head = malloc(sizeof(listint_t));
	second = malloc(sizeof(listint_t));
	third = malloc(sizeof(listint_t));

	head->n = 1;
	head->next = second;
	
	second->n = 2;
	second->next = third;

	third->n = 3;
	third->next = head;
	
	if (check_cycle(head))
		printf("Cycle detected!\n");
	else
		printf("No cycle found.\n");

	free(head);
	free(second);
	free(third);

	return (0);
}
