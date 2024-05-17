class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_in_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_at_front(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def delete_at_back(self):
        if not self.head:
            return None
        if not self.head.next:
            value = self.head.data
            self.head = None
            return value
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        value = second_last.next.data
        second_last.next = None
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
        def _print_backward(node):
            if not node:
                return
            _print_backward(node.next)
            print(node.data, end=" ")
        _print_backward(self.head)
        print()  # for a new line

    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_recursive(next_node, current)
        self.head = _reverse_recursive(self.head, None)

    def reverse_non_recursive(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


ll = SinglyLinkedList()
ll.insert_in_back(1)
ll.insert_in_back(2)
ll.insert_in_back(3)
ll.print_forward()  

ll.insert_in_front(10)
ll.print_forward()  

print(ll.delete_at_front())  
ll.print_forward()  

print(ll.delete_at_back()) 
ll.print_forward() 

print(ll.search(1))  
print(ll.search(2))  

ll.clear()
ll.print_forward()  

ll.insert_in_back(1)
ll.insert_in_back(2)
ll.insert_in_back(3)
print(ll.size())  

ll.print_forward()  
ll.print_backward() 

ll.reverse_recursive()
ll.print_forward()  

ll.reverse_non_recursive()
ll.print_forward() 
