#include <stdio.h>
#include <stdlib.h>

// Node structure
typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;

// Global head pointer for simplicity in this example
Node *head = NULL;

// Function to create a new node
Node *createNode(int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

// Function to insert a node at the end (maintaining circularity)
void insertEnd(int data) {
    Node *newNode = createNode(data);
    
    if (head == NULL) {
        // First node: points to itself (circular)
        head = newNode;
        head->next = head;
        head->prev = head;
    } else {
        Node *tail = head->prev; // Get the current tail
        
        newNode->prev = tail;
        newNode->next = head;
        
        tail->next = newNode;
        head->prev = newNode;
    }
}

// Function to delete a node with a specific data value
void deleteNode(int data) {
    if (head == NULL) return;

    Node *current = head;
    
    // Loop until we find the node or we loop back to head
    do {
        if (current->data == data) {
            // Case 1: Only one node in the list
            if (current->next == current) {
                free(current);
                head = NULL;
                return;
            }
            
            // Case 2: Node is the head
            if (current == head) {
                head = current->next; // New head
            }
            
            // Re-wire the previous and next nodes
            current->prev->next = current->next;
            current->next->prev = current->prev;
            
            free(current);
            return;
        }
        current = current->next;
    } while (current != head);
}

// Function to print the circular list (up to 10 nodes to prevent infinite loop)
void display() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }
    Node *current = head;
    int count = 0;
    
    printf("Circular List: ");
    do {
        printf("%d -> ", current->data);
        current = current->next;
        count++;
    } while (current != head && count < 10); // Safety limit for display
    printf("(Back to %d)\n", head->data);
}

int main() {
    insertEnd(10);
    insertEnd(20);
    insertEnd(30);
    display(); // Output: Circular List: 10 -> 20 -> 30 -> (Back to 10)
    
    deleteNode(20);
    display(); // Output: Circular List: 10 -> 30 -> (Back to 10)
    
    deleteNode(10);
    deleteNode(30);
    display(); // Output: List is empty.

    return 0;
}