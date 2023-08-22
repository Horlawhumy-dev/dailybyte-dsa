

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Dequeue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    
    def enqueue(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

dq =  Dequeue()
dq.enqueue(5)
dq.enqueue(6)
dq.enqueue(7)

print(dq.count)
    
    # def __str__(self):

    #     current = self.head

    #     while current.next and current.next.data != self.tail:
    #         print()
    #     return 