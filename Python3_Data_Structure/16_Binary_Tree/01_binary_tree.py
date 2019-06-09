

"""

Python - Binary Tree

Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties.

One node is marked as Root node.
Every node other than the root is associated with one parent node.
Each node can have an arbiatry number of chid node.
We create a tree data structure in python by using the concept os node discussed earlier. We designate one node as
 root node and then add more nodes as child nodes. Below is program to create the root node.

Create Root
We just create a Node class and add assign a value to the node. This becomes tree with only a root node.


"""

class Node:
    
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)

root = Node(10)

root.PrintTree()


"""

When the above code is executed, it produces the following result −

10

"""




