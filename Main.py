from Node import Node
parent = Node(10)
parent.add_node(11)
parent.add_node(8)
parent.add_node(12)
parent.add_node(4)
parent.add_node(10)


print(parent.size)


COUNT =[10]
def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right_child, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.value)
 
    # Process left child
    print2DUtil(root.left_child, space)
 
# Wrapper over print2DUtil()
print2DUtil(parent, 5)