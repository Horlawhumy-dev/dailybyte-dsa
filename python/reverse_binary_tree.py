

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):

        if not self.is_emtpy():
            return self.items.pop()

    def is_emtpy(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_emtpy():
            return self.items[-1]
        
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
        

class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def traverse_level_order_for(self, root):

        if root is None:
            return
        
        queue = Queue()
        queue.enqueue(root)
        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            traversal += str(node.data) + "-"

            if node.left is not None:
                queue.enqueue(node.left)
            
            if node.right is not None:
                queue.enqueue(node.right)

        return traversal
    
    def revese_tree(self, root):

        if root is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(root)

        reversal = ""
        while len(queue) > 0:

            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)

            if node.left:
                queue.enqueue(node.left)

        while len(stack):

            node = stack.pop()

            reversal += str(node.data) + "-"

        return reversal

    def size_(self, node):

        if node is None:
            return 0
        
        queue = Queue()

        queue.enqueue(node)
        count = 0

        while len(queue) > 0:

            node = queue.dequeue()

            count += 1

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return count

            
bt = BinaryTree(1)

bt.root.left = Node(2)
bt.root.right = Node(3)

bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)


print(bt.size_(bt.root))