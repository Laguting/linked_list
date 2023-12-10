class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_valid_range(self, data):
        return 0 <= data <= 50

    def insert_at_beginning(self, data):
        if not self.is_valid_range(data):
            print("Invalid input. Please enter a value between 0 and 50.")
            return

        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        if not self.is_valid_range(data):
            print("Invalid input. Please enter a value between 0 and 50.")
            return

        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

def merge_linked_lists(list1, list2):
    merged_list = LinkedList()

    current_node1 = list1.head
    current_node2 = list2.head

    while current_node1 is not None and current_node2 is not None:
        if current_node1.data < current_node2.data:
            merged_list.insert_at_end(current_node1.data)
            current_node1 = current_node1.next
        else:
            merged_list.insert_at_end(current_node2.data)
            current_node2 = current_node2.next

    while current_node1 is not None:
        merged_list.insert_at_end(current_node1.data)
        current_node1 = current_node1.next

    while current_node2 is not None:
        merged_list.insert_at_end(current_node2.data)
        current_node2 = current_node2.next

    return merged_list

list1 = LinkedList()

while True:
    value = int(input("Enter a value between 0 and 50 for the first linked list (or -1 to stop): "))
    
    if value == -1:
        break
    
    list1.insert_at_end(value)

list2 = LinkedList()

while True:
    value = int(input("Enter a value between 0 and 50 for the second linked list (or -1 to stop): "))
    
    if value == -1:
        break
    
    list2.insert_at_end(value)
    

merged_list = merge_linked_lists(list1, list2)
print("Merged Linked List:")
merged_list.printLinkedList()
