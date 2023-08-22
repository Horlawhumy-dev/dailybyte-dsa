

from collections import deque


class Node:

    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None



class BST:

    def __init__(self):
        self.root_node = None
        self.count = 0

    
    def insert(self, data):
        new_node = Node(data)

        if self.root_node is None:
            self.root_node = new_node
            self.count += 1
            return
        

        current = self.root_node

        while True:

            parent = current

            if new_node.data < current.data:

                current = current.left_child

                if current is None:

                    parent.left_child = new_node
                    break
                
            else:
                current = current.right_child

                if current is None:

                    parent.right_child = new_node

                    break
        
        self.count += 1
        return
    

    def find_minimum(self):

        current = self.root_node

        while current.left_child is not None:

            current = current.left_child

        return current.data
    

    def find_maximum(self):

        current = self.root_node

        while current.right_child is not None:

            current = current.right_child

        return current.data
        

    def get_node_with_parent(self, data):

        parent = None

        current = self.root_node

        if current is None:
            return (parent, None)
        
        while True:

            if current.data == data:
                return (parent, current)
        
            elif data < current.data:
                parent = current
                current = current.left_child
            
            else:
                parent = current
                current = current.right_child


    def delete(self, data):
        parent, node = self.get_node_with_parent(data)
        child_count = 0

        if parent is None and node is None:
            return None
        
        if parent.right_child is not None and parent.left_child is not None:
            child_count = 2
        elif parent.right_child is None and parent.left_child is None:
            child_count = 0
        else:
            child_count = 1

        if child_count == 0:
            if parent:
                if parent.left_child is node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None
            self.count -= 1
            return
        
        elif child_count == 1:
            print(child_count)
            next_node = None

            if node.left_child is not None:
                next_node = node.left_child

            else:
                next_node = node.right_child

            if parent:

                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node

            else:
                self.root_node = next_node
                self.count -= 1
                return

        self.count -= 1
        # else:

        #     parent_of_leftmost_node = node

        #     leftmost_node = node.right_child

        #     while leftmost_node.left_child is not None:

        #         parent_of_leftmost_node = leftmost_node
        #         leftmost_node = leftmost_node.left_child

        #     node.data = leftmost_node.data

        #     if parent_of_leftmost_node.left_child == leftmost_node:
        #         parent_of_leftmost_node.left_child = leftmost_node.right_child
        #     else:
        #         parent_of_leftmost_node.right_child = leftmost_node.right_child


    def search(self, root_node, data):

        current = root_node

        if current is None:
            return None

        if current.data == data:
            return current.data
        
        if data < current.data:
            value = self.search(current.left_child, data)

        
        if  data > current.data:
            value = self.search(current.right_child, data)

        return value
    
    # Depth-first Traversal methods
    def inorder(self, root_node):
        """ LEFT -> ROOT -> RIGHT """
        current = root_node

        if current is None:
            return
        
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):
        """ ROOT -> LEFT -> RIGHT """
        current = root_node

        if current is None:

            return
        
        print(f"{current.data} \n")

        self.preorder(current.left_child)
        # print("started calling right nodes")
        self.preorder(current.right_child)

    def postorder(self, root_node):
        """ LEFT -> RIGHT -> ROOT """
        current = root_node

        if current is None:
            return
        
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)

    #Breadth-first Traversal
    def breadth_first_traversal(self):
        """ VISIT NODES LEVEL BY LEVEL (PARENT -> LEFT -> RIGHT)"""
        visited_nodes_data = list()

        traversal_nodes_queue = deque([self.root_node])

        while len(traversal_nodes_queue) > 0:

            node = traversal_nodes_queue.popleft()

            visited_nodes_data.append(node.data)

            if node.left_child:
                traversal_nodes_queue.append(node.left_child)

            if node.right_child:
                traversal_nodes_queue.append(node.right_child)

        return visited_nodes_data




bst = BST()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(10)
# bst.insert(2)
# bst.insert(1)
# bst.insert(3)

min_child = bst.find_minimum()
max_child = bst.find_maximum()


print(f"The total children of the BST is {bst.count}")
print(f"Minimum child is {min_child} and Maximum value among chilren is {max_child}")

# bst.inorder(bst.root_node)
# bst.preorder(bst.root_node)
print(bst.breadth_first_traversal())