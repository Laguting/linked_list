class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
 
 
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail=new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head=new_node


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

# Example usage:
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)

list2 = LinkedList()
list2.insert_at_end(1)
list2.insert_at_end(2)
list2.insert_at_end(5)

merged_list = merge_linked_lists(list1, list2)
merged_list.printLinkedList()
