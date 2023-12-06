class Node:
    def __init__(self, value):
        '''
        self 
        parent int: the size of the root node to the new node 
        size int: the size of the node   
        '''
        self.value = value
        self.left_child = None
        self.right_child = None
        self.c = 0.5
        self.size = 1
    def add_node(self,value):
        '''
        Add a child node to the tree and iff the node is smaller the the root
        it is the left child node else the right child node

        size int: the size off the new node
        '''
        self.size += 1
        try: 
            #self.c*self.size < self.left_child.size or self.c*self.size < self.left_child.size
            X = None*2
        except:
            if value < self.value:
                if self.left_child is not None:
                    self.left_child.add_node(value)
                else:
                    self.left_child = Node(value)
            elif value >= self.value:
                if self.right_child is not None:
                    self.right_child.add_node(value)
                else:
                    self.right_child = Node(value)
        else:
            print('error subtree to', self.size)
            print(f'eq L: {self.c}*{self.size} > {self.left_child.size}')
            print(f'eq R: {self.c}*{self.size} > {self.right_child.size}')
        
        

   
    
