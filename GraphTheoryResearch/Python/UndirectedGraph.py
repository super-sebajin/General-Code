#Author: Sebastian R. Papanikolaou Costa
#Here will be housed a set of classes that will be used to model an arbitrary 
#Unidrected Graph. The purpose of these classes will be to use proper OOP concepts
#for modeling these mathematical objects.

#A graph G(V,E) is the set G(V,E) = {V, E}, where V = {v1...,vn} and
#E = {{v1,v2},...{vn,v(n+1)}}. Therefore, this module will be comprised of the
#following classes:
#  GraphVertex:
#     deg: Integer
#     _incidence_list: [GraphEdge]
#     data: Object
#     
#
#  GraphEdge: (with respect to common data structures, GraphEdge is designed to act as a node from a doubly linked list or it circular variant)
#     vertex_left: GraphVertex
#     vertex_right: GraphVertex
#     _update_incidence_lists(): Void

#class GraphVertex: class model of a general graph vertex.
class GraphVertex:
    #area for class attributes

    #Constructor
    def __init__(self, data=None):
        self._degree = 0 #Any graph construction starts with their vertices at deg(vn)=0
        self._incidence_list = list()
        self._data = data
  
    #property decorator for get/set operations for self._data
    @property
    def data(self):
        return(self._data)

    @data.setter
    def data(self,new_data):
        self._data = new_data

     #property decorator for get/set operation for self._incidence_list
    @property
    def incidence_list(self):
        return(self.incidence_list)
    
    #property decorator for self._degree for get operations, the setter for this function
    @property #will be defined in this class' subclasses
    def degree(self):
        return(self._degree)
    @degree.setter
    def degree(self, new_degree):
        self._degree = new_degree
  


  #class GraphEdge: class model of a general graph edge
class GraphEdge:
    #are for class attributes

    def __init__(self, vertex_a= None, vertex_b= None):
        self._vertex_a = vertex_a
        self._vertex_b = vertex_b
        self._connect_vertices()
    
    #code that "updates" the GraphVertex objects about the edge and the connection
    def _update_incidence_list(self):
        self._vertex_a.incidence_list.append(self)
        self._vertex_b.incidence_list.append(self)
    def _update_vertex_degrees(self):
        self._vertex_a.degree += 1
        self._vertex_b.degree += 1
    def _connect_vertices(self):
        self._update_incidence_list()
        self._update_vertex_degrees()



     

  

