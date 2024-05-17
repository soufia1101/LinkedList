class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        new_node = DoublyNode(value)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_in_back(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_at_front(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return value

    def delete_at_back(self):
        if not self.head:
            return None
        if not self.head.next:
            value = self.head.data
            self.head = None
            return value
        last = self.head
        while last.next:
            last = last.next
        value = last.data
        last.prev.next = None
        return value

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def clear(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

    def print_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" ".join(elements))

    def reverse_recursive(self):
        def _reverse_recursive(current):
            if not current:
                return None
            current.next, current.prev = current.prev, current.next
            if not current.prev:
                return current
            return _reverse_recursive(current.prev)
        self.head = _reverse_recursive(self.head)

    def reverse_non_recursive(self):
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def shift(self, num):
        if not self.head or num == 0:
            return
        size = self.size()
        num = num % size
        if num < 0:
            num += size
        if num == 0:
            return
        
        current = self.head
        for _ in range(size - num - 1):
            current = current.next
        new_head = current.next
        current.next = None
        new_head.prev = None
        
        last = new_head
        while last.next:
            last = last.next
        last.next = self.head
        self.head.prev = last
        self.head = new_head

def make_doubly(singly_linked_list):
    doubly_linked_list = DoublyLinkedList()
    current = singly_linked_list.head
    while current:
        doubly_linked_list.insert_in_back(current.data)
        current = current.next
    return doubly_linked_list


sll = SinglyLinkedList()
sll.insert_in_back(1)
sll.insert_in_back(2)
sll.insert_in_back(3)
sll.insert_in_back(4)
sll.insert_in_back(5)

dll = make_doubly(sll)
dll.print_forward()  

dll.shift(2)
dll.print_forward()  

dll.shift(-1)
dll.print_forward()  
