


class Stack:

    def __init__(self):

        self.items = list()
        self.count = 0


    def push(self, data):
        self.items.append(data)
        self.count += 1

    def pop(self):
        popped_off = self.items.pop()
        self.count -= 1
        return popped_off


class TreeNode:

    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def perform_bst_operation(self, value):
        """ 4 5 + 5 3 - * """
        splitted_vals = value.split() # ["4", "5", "+", "5", "3", "-", "*"]
        
        stack = self.get_tree_stack_for(splitted_vals)

        root = stack.pop()
        result = self.calulate_for(root)

        return result

    def get_tree_stack_for(self, list_of_vals):
        stack = Stack()

        for val in list_of_vals:

            if val in "+-*":

                tree_node = TreeNode(val)
                tree_node.right = stack.pop()
                tree_node.left = stack.pop()
            else:
                tree_node = TreeNode(int(val))
            
            stack.push(tree_node)

        return stack.items
    
    def calulate_for(self, node):

        if node.data == "+":
            return self.calulate_for(node.left) + self.calulate_for(node.right)

        elif node.data == "-":
            return self.calulate_for(node.left) - self.calulate_for(node.right)
        
        elif node.data == "*":
            return self.calulate_for(node.left) * self.calulate_for(node.right)
        
        else:
            return node.data
        


tr = TreeNode()
print(tr.perform_bst_operation("4 5 + 5 3 - *"))