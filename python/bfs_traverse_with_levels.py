from collections import deque


class TreeNode:

    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None
    
    def bfs_traverse_with_levels(self, root):

        if root is None:
            return
        
        queue = deque()

        # forward_order_level = []
        # reverse_order_level = []
        level_averages = []
        max_value_by_level = []
        queue.append(root)

        left_to_right = True

        while queue:
            
            level_size = len(queue)
            current_level_nodes = []
            level_sum = 0
            max_value = 0
            for _ in range(level_size):
                
                popped_node = queue.popleft()

                if left_to_right:

                    current_level_nodes.append(popped_node.data)
                else:
                    current_level_nodes.insert(0, popped_node.data)
                    
                level_sum += popped_node.data
                max_value = max(max_value, popped_node.data)

                if popped_node.left_child:
                    queue.append(popped_node.left_child)

                if popped_node.right_child:
                    queue.append(popped_node.right_child)

                    
            # forward_order_level.append(current_level_nodes) #will give level-by-level in forward order
            # reverse_order_level.insert(0, current_level_nodes) #will give level-by-level in reverse order
            left_to_right = not left_to_right
             
            average = level_sum / len(current_level_nodes)
            level_averages.append(average)
            max_value_by_level.append(max_value)
        # return (forward_order_level, reverse_order_level)
        return level_averages, max_value_by_level

root_node = TreeNode(12)
root_node.left_child = TreeNode(7)
root_node.right_child = TreeNode(8)
root_node.left_child.left_child = TreeNode(3)
root_node.left_child.right_child = TreeNode(4)
root_node.right_child.left_child  = TreeNode(6)
root_node.right_child.right_child  = TreeNode(9)

print(root_node.bfs_traverse_with_levels(root_node))


