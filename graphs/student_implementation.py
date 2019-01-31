from collections import namedtuple

# Named tuple instead of class, for berveity.
Edge = namedtuple('Edge', ('from_name', 'to_name', 'weight'))

class UndirectedGraph:
    '''
    An undirected graph.
    '''
    def __init__(self):
        '''
        A new graph never has any nodes or edges.
        '''
        pass


    def add_node(self, name):
        '''
        Create a new node and add it to the graph. Name must be a hashable type.

        return value indicates if a node was actually added, True means a new
        node was created and added, False means that a node with that name already
        exists in this graph, and it was not overwritten.
        '''
        pass


    def add_edge(self, a_name, b_name, weight = 1):
        '''
        Create an edge between a and b with the provided weight.

        If either of the names is not already a member of the graph, create
        that node and add it to the graph first.
        '''
        pass


    def neighbors(self, from_name):
        '''
        Return an iterator that yields (name, weight) of all the neighboring nodes.
        '''
        pass


    def contains(self, name):
        '''
        Return true if the name already maps to a node, false otherwise
        '''
        pass


    def nodes(self):
        '''
        Return an iterator that yields the node names (in no particular order)
        '''
        pass


    def edges(self):
        '''
        Return all the edges as an iterator of Edges (named tuples) with values
        (from_name, to_name, weight). Edges are yielded in no particular order.
        '''
        pass


class DirectedGraph:
    '''
    An undirected graph.
    '''
    def __init__(self):
        '''
        A new graph never has any nodes or edges.
        '''
        pass

    def add_node(self, name):
        '''
        Create a new node and add it to the graph. Name must be a hashable type.

        return value indicates if a node was actually added, True means a new
        node was created and added, False means that a node with that name already
        exists in this graph, and it was not overwritten.
        '''
        pass

    def add_edge(self, a_name, b_name, weight = 1):
        '''
        Create an edge between a and b with the provided weight.

        If either of the names is not already a member of the graph, create
        that node and add it to the graph first.
        '''
        pass


    def neighbors(self, from_name):
        '''
        Return an iterator that yields (name, weight) of all the neighboring nodes.
        '''
        pass


    def contains(self, name):
        '''
        Return true if the name already maps to a node, false otherwise
        '''
        pass


    def nodes(self):
        '''
        Return an iterator that yields the node names (in no particular order)
        '''
        pass


    def edges(self):
        '''
        Return all the edges as an iterator of Edges (named tuples) with values
        (from_name, to_name, weight). Edges are yielded in no particular order.
        '''
        pass
