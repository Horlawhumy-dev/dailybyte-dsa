from collections import deque

class TreeNode:

    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None


    def bfs_level_order_successor(self, root, given_node):

        if  root is None or given_node is None:

            return 0
        
        queue = deque()
        queue.append(root)
        while queue:
            current_node = queue.popleft()

            if current_node.left_child: 
                queue.append(current_node.left_child)

            if current_node.right_child:
                queue.append(current_node.right_child)

            if current_node.data == given_node.data:
                break
                
        return queue[0].data if queue else None
                
        
    

root_node = TreeNode(12)
root_node.left_child = TreeNode(7)
root_node.right_child = TreeNode(8)
root_node.left_child.left_child = TreeNode(3)
root_node.left_child.right_child = TreeNode(4)
root_node.right_child.left_child  = TreeNode(6)
root_node.right_child.right_child  = TreeNode(9)

print(root_node.bfs_level_order_successor(root_node, TreeNode(8)))