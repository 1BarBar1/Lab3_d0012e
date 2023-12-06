class Node:
    def __init__(self, size):
        '''
        self 
        parent int: the size of the root node to the new node 
        size int: the size of the node   
        '''
        self.size = size
        self.left_child = None
        self.right_child = None
        self.c = 0.5
        
    def add_node(self,size):
        '''
        Add a child node to the tree and iff the node is smaller the the root
        it is the left child node else the right child node

        size int: the size off the new node
        '''
        if size < self.size and self.c*size < self.size:
            if self.left_child is not None:
                self.left_child.add_node(size)
            else:
                self.left_child = Node(size)
        elif size >= self.size and self.c*size < self.size:
            if self.right_child is not None:
                self.right_child.add_node(size)
            else:
                self.right_child = Node(size)
        elif self.c*size > self.size:
            

    def give_nodesize(self):
        return self.size
        
    
