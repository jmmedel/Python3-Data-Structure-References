


"""

Python - Graphs

A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. 
The interconnected objects are represented by points termed as vertices, and the links that connect the vertices
 are called edges. The various terms and functionalities associated with a graph is described in great detail in our
  tutorial here. In this chapter we are going to see how to create a graph and add various data elements to it using 
  a python program. Following are the basic operations we perform on graphs.

Display graph vertices
Display graph edges
Add a vertex
Add an edge
Creating a graph
A graph can be easily presented using the python dictionary data types. We represent the vertices as the keys of the 
dictionary and the connection between the vertices also called edges as the values in the dictionary.

Take a look at the following graph −

"""


# Create the dictionary with graph elements
graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

# Print the graph 		 
print(graph)


"""

When the above code is executed, it produces the following result −

{'c': ['a', 'd'], 'a': ['b', 'c'], 'e': ['d'], 'd': ['e'], 'b': ['a', 'd']}

"""
