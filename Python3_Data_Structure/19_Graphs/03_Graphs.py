


"""

Adding a vertex
Adding a vertex is straight forward where we add another additional key to the graph dictionary.

"""

class graph:
    
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

# Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

g.addVertex("f")

print(g.getVertices())



"""

When the above code is executed, it produces the following result −

['a', 'b', 'c', 'd', 'e', 'f']


"""
