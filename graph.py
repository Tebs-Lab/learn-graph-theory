class Graph:
    '''
    An undirected graph.
    '''
        def __init__(self):
            '''
            A new graph never has any nodes or edges.
            '''
            pass


        def add_node(name):
            '''
            Create a new node and add it to the graph. Name must be a hashable type.
            '''
            pass


        def add_edge(a_name, b_name, weight = 1):
            '''
            Create an edge between a and b with the provided weight.
            '''
            pass


        def neighbors(from_name):
            '''
            Return the names of all the neighboring nodes.
            '''
            pass


        def edges():
            '''
            Return all the edges as a list of tupels (from_name, to_name).
            '''
            pass


class DirectedGraph:
    '''
    A directed Graph
    '''
    def __init__(self):
        '''
        A new graph never has any nodes or edges.
        '''
        pass


    def add_node(name):
        '''
        Create a new node and add it to the graph. Name must be a hashable type. 
        '''
        pass


    def add_edge(from_name, to_name, weight = 1):
        '''
        Create an edge from from_name to to_name, provided those identify nodes.
        '''
        pass


    def neighbors(from_name):
        '''
        Return the names of all the neighboring nodes.
        '''
        pass


    def edges():
        '''
        Return all the edges as a list of tupels (from_name, to_name).
        '''
        pass
