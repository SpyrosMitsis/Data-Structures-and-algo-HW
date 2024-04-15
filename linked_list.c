#include <stdio.h>
#include <stdlib.h>


struct Node {
    int data;
    struct Node *next;
};


struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL){
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}


int insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;

    return 0;
}

void printList(struct Node** head) {
    struct Node* temp = *head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    struct Node *iterator = *head;

    while (iterator->next != NULL) {
        iterator = iterator->next;
    }

    iterator->next = newNode;
    return 0;
}

int deleteAtEnd(struct Node** head) {

    struct Node *iterator = *head;
    struct Node *previous = NULL;

    while (iterator->next !=NULL) {
        previous = iterator;
        iterator = iterator->next;
    }
    previous->next = NULL;
    free(iterator);

    return 0;
}

int deleteAtBeginning(struct Node** head) {
    struct Node *current = *head;
    *head = current->next;
    free(current);
    return 0;

}

int deleteNode(struct Node** head, int data) {
    struct Node *current = *head;
    struct Node *previous = NULL;

    if (current != NULL && current->data == data) {
        *head = current->next;
        free(current);
        return 0;
    }

    while (current != NULL && current->data != data){
        previous = current;
        current = current->next;
    }

    if (current !=NULL) {
        previous->next = current->next;
        free(current);
        return 0;
    }
    return -1;
}

int main() {
    struct Node* head = NULL;


    insertAtBeginning(&head, 45);
    insertAtBeginning(&head, 5);
    insertAtBeginning(&head, 1);
    printf("Printend list\n");
    printList(&head);
    //deleteNode(&head, 5);
    deleteAtBeginning(&head);
    printList(&head);
    insertAtEnd(&head, 990);
    printList(&head);
    deleteAtEnd(&head);
    printList(&head);

    return 0;
}