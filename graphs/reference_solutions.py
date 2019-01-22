from collections import namedtuple

# Named tuple instead of class, for berveity
Edge = namedtuple('Edge', ('from_name', 'to_name', 'weight'))

class UndirectedGraph:
    '''
    An undirected graph.
    '''
    def __init__(self):
        '''
        A new graph never has any nodes or edges.
        '''
        self._adjacency_table = {}


    def add_node(self, name):
        '''
        Create a new node and add it to the graph. Name must be a hashable type.

        return value indicates if a node was actually added, True means a new
        node was created and added, False means that a node with that name already
        exists in this graph, and it was not overwritten.
        '''
        if self._adjacency_table.get(name) != None:
            return False

        self._adjacency_table[name] = {}
        return True


    def add_edge(self, a_name, b_name, weight = 1):
        '''
        Create an edge between a and b with the provided weight.

        If either of the names is not already a member of the graph, create
        that node and add it to the graph first.
        '''
        if self._adjacency_table.get(a_name) == None:
            self.add_node(a_name)

        if self._adjacency_table.get(b_name) == None:
            self.add_node(b_name)

        self._adjacency_table[a_name][b_name] = weight
        self._adjacency_table[b_name][a_name] = weight


    def neighbors(self, from_name):
        '''
        Return an iterator that yields (name, weight) of all the neighboring nodes.
        '''
        adj_nodes = self._adjacency_table.get(from_name)
        if adj_nodes is None:
            return

        return adj_nodes.items()


    def contains(self, name):
        '''
        Return true if the name already maps to a node, false otherwise
        '''
        return self._adjacency_table.get(name) != None


    def nodes(self):
        '''
        Return an iterator that yields the node names (in no particular order)
        '''
        return self._adjacency_table.keys()


    def edges(self):
        '''
        Return all the edges as an iterator of Edges (named tuples) with values
        (from_name, to_name, weight). Edges are yielded in no particular order.
        '''
        for from_name, adj_dict in self._adjacency_table.items():
            for to_name, weight in adj_dict.items():
                yield Edge(from_name, to_name, weight)

class DirectedGraph:
    '''
    An undirected graph.
    '''
    def __init__(self):
        '''
        A new graph never has any nodes or edges.
        '''
        self._adjacency_table = {}


    def add_node(self, name):
        '''
        Create a new node and add it to the graph. Name must be a hashable type.

        return value indicates if a node was actually added, True means a new
        node was created and added, False means that a node with that name already
        exists in this graph, and it was not overwritten.
        '''
        if self._adjacency_table.get(name) != None:
            return False

        self._adjacency_table[name] = {}
        return True


    def add_edge(self, a_name, b_name, weight = 1):
        '''
        Create an edge between a and b with the provided weight.

        If either of the names is not already a member of the graph, create
        that node and add it to the graph first.
        '''
        if self._adjacency_table.get(a_name) == None:
            self.add_node(a_name)

        if self._adjacency_table.get(b_name) == None:
            self.add_node(b_name)

        self._adjacency_table[a_name][b_name] = weight


    def neighbors(self, from_name):
        '''
        Return an iterator that yields (name, weight) of all the neighboring nodes.
        '''
        adj_nodes = self._adjacency_table.get(from_name)
        if adj_nodes is None:
            return

        return adj_nodes.items()


    def contains(self, name):
        '''
        Return true if the name already maps to a node, false otherwise
        '''
        return self._adjacency_table.get(name) != None


    def nodes(self):
        '''
        Return an iterator that yields the node names (in no particular order)
        '''
        return self._adjacency_table.keys()


    def edges(self):
        '''
        Return all the edges as an iterator of Edges (named tuples) with values
        (from_name, to_name, weight). Edges are yielded in no particular order.
        '''
        for from_name, adj_dict in self._adjacency_table.items():
            for to_name, weight in adj_dict.items():
                yield Edge(from_name, to_name, weight)
