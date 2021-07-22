#These classes are part of a conitnued research effort on my part. The
#original purpose comes from research on De Bruijn sequences. The idea is to
#construct these sequences from De Bruijn Graphs. This was in hopes
#to create matrices (square) whose entries are symbols of a De Bruijn sequence.
#However it proved to be a bit more difficul than expected. I have since then g
#and my time permits me to delve in to this a bit more. I will attempt to 
#construct the 16 sequences that comprise the (2,4) De Bruijn sequences. 
#The current approach is to consider a circular doubly linked list to represent
#a Hamiltonian cycle on a general digraph by using a sorting algorithm. This
#code, however is just to demonstrate a rough model a digraph vertex and edge.


#Standard practice is to represent a graph using a dictionary, vertices will
#actually act as list and tree nodes (linked lists, doubly linked lists).
#We know that nodes have a tails and a heads that point to the other
#nodes in the tree or list.

class DiGraphVertex:
    """
    Keyword Arguments: key <- the actual value stored in the vertex
    
    Attributes:
        - key:Object <- value stored in the vertex, termed key for traversals
        - in_deg:Integer <- Number of incoming edges
        - out_deg:Integer <- Number of outgoing edges
        - in_list:set:DirectedEdge <- Set of all incoming DirectedEdge objects
        - out_list:set:DirectedEdge <- Set of all outgoing DirectedEdge object
    """
    def __init__(self, key=None):
        self.key = key 
        self.in_deg = 0
        self.out_deg = 0
        self.incidence_list = list()
        

class DirectedEdge:
    """
    Directed edge will be used in DiGraphVertex, and will
    simply contain two references to two distinct vertices
    """
    def __init__(self, tail_vertex=None, head_vertex=None):
        #assign the tail and head of this edge
        self.tail_vertex = tail_vertex
        self.head_vertex = head_vertex
        self.update_vertices()
        
    #update the degree counts of each connected vertex
    def update_vertices(self):
        #update the in/out degrees of the vertices the edge connects
        self.tail_vertex.out_deg = self.tail_vertex.out_deg + 1
        self.head_vertex.in_deg = self.head_vertex.in_deg + 1
        #update each vertex so that it is 'aware' of the edge
        self.tail_vertex.incidence_list.append(self)
        self.head_vertex.incidence_list.append(self)
        
        
    #return a tuple holding 
    def get_vertices(self):
        return (self.tail_vertex, self.head_vertex)