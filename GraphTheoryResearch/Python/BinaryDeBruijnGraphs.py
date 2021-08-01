#Author: Sebastian R. Papanikolaou Costa
#These classes are part of a conitnued research effort on my part. The
#original purpose comes from research on De Bruijn sequences. The idea is to
#construct these sequences from De Bruijn Graphs. This was in hopes
#to create matrices (square) whose entries are symbols of a De Bruijn sequence.
#However it proved to be a bit more difficul than expected. I have since then g
#and my time permits me to delve in to this a bit more. I will attempt to 
#construct the 16 sequences that comprise the (2,4) De Bruijn sequences. 
#The current approach is to consider a circular doubly linked list to represent
#a Hamiltonian cycle on a general digraph by using a sorting algorithm. 


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

        
#class DeBruijGraph: scratch code (meant for test, final version may or may not
#implement methods from this class or even used at all). 
class BinaryDeBruijnGraph:
    symbols = [0,1]
    """
    This class assumes that the symbols inserted are symbols from the binary field.
    """
    def __init__(self, key_list=None):
        self.vertex_list = []
        self.edge_list = []
        #key_list is asssumed to be populated, this section we popoulate self.vertex_list
        if key_list != None:
            for curr_key in key_list:#iterate through each key in the list
                curr_vertex = DiGraphVertex(curr_key)#initialize a DiGraphVertex object and name it curr-vertex
                self.vertex_list.append(curr_vertex)#append curr_vertex to self.vertex_list
        #Here, we first initialize each edge, connect the two vertices incident to it
        self._make_edge_list(self.vertex_list)
    
    #define a method to initialize a DirectedEdge objects, this
    #takes the tail and head vertices as arguments. This will be
    #used in another method.
    def _connect_vertices(self, vertex_a, vertex_b):
        #If one of the vertices can be expressed as another vertex by 
        #shifting all its symbols by one place to the left and adding 
        #a new symbol at the end of this vertex, then the latter has 
        #a directed edge to the former vertex. This method use the formal 
        #definition of a De Bruijn Graph found in its Wikipedia article wikipedia.org/wiki/De_Bruijn_graph
        import copy#shallow copy two have two test cases arising from the other_vertex
        curr_vertex = list(vertex_a.key)
        other_vertex = list(vertex_b.key)
        other_vertex.pop(0)
        test_1 = copy.copy(other_vertex)
        test_2 = copy.copy(other_vertex)
        test_1.append(self.symbols[1])
        test_2.append(self.symbols[0])
        if curr_vertex == test_1:
            self.edge_list.append(DirectedEdge(vertex_b, vertex_a))
        elif curr_vertex == test_2:
            self.edge_list.append(DirectedEdge(vertex_b, vertex_a))
    
    def _make_edge_list(self, vertices):
        for current_vertex_index in range(len(vertices)):
            for other_vertex in vertices:
                self._connect_vertices(vertices[current_vertex_index], other_vertex)   
            
    #dunder methods for pythonic behaviour, it helps for testing. PYTHON!!        
    def __str__(self):
        _str = "Current De Bruin Graph:\nVertices: {} in total.\n[\n".format(len(self.vertex_list))
        for vertex in self.vertex_list:
            _str = _str + "{},\n".format(vertex.key)
        _str = _str + "]\n\rEdges:{}\n[\n".format(len(self.edge_list))
        for edge in self.edge_list:
            _str = _str + "{},{}\n".format(edge.tail_vertex.key, edge.head_vertex.key)
        _str = _str + "]"
        return(_str)
        