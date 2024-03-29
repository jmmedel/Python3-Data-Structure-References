


"""

Post-order Traversal
In this traversal method, the root node is visited last, hence the name.
 First we traverse the left subtree, then the right subtree and finally the root node.

In the below python program, we use the Node class to create place holders for the root 
node as well as the left and right nodes. Then we create a insert function to add data to
 the tree. Finally the Post-order traversal logic is implemented by creating an empty list 
 and adding the left node first followed by the right node. At last the root or parent node 
 is added to complete the Post-order traversal. Please note that this process is repeated for 
 each sub-tree until all the nodes are traversed.


"""

class Node:
    
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Postorder traversal
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PostorderTraversal(root))

"""

When the above code is executed, it produces the following result −

[10, 19, 14, 31, 42, 35, 27]

"""


