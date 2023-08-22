from collections import deque


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def find_bst_mode(self, root):

        if root == None:

            return -1

        queue = deque()

        queue.append(root)

        nodes_dict  = dict()

        while len(queue) > 0:

            current_node = queue.popleft()
            # print(current_node.data)

            if nodes_dict.get(current_node.data, 0) == 0:

                nodes_dict[current_node.data] = 1
            else:

                nodes_dict[current_node.data] += 1

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        mode = 0
        max_node = []
        for data, val in nodes_dict.items():
            if val > mode:
                # del nodes_dict[data]
                mode = val
                max_node.append(data)

        return max_node
    
    
    



root = TreeNode(1)
root.left = TreeNode(None)
root.right = TreeNode(2)
root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(8)
# root.right.right = TreeNode(9)
# root.right.right.right = TreeNode(9)

print(root.find_bst_mode(root))