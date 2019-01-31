# Feel free to define any helper functions, or import anything from this repo or
# the standard library. The parameter g will always be a graph, your algorithms
# should work for both DriectedGraphs and UndirectedGraphs.

def breadth_first_search(g, start_node, stop_node):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and stop_node, using bfs determine if there is a path between the two nodes. If
    there is a path return a list containing the names of the nodes that comprise the path
    in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    pass


def breadth_first_search_by_criteria(g, start_node, stop_criteria):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and a function stop_criteria, using bfs determine if there is a path between the
    start_node and any node matching the stop_criteria. Nodes match the criteria if
    stop_criteria(node) == True

    If there is a path return a list containing the names of the nodes that
    comprise the path in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    pass

def depth_first_search(g, start_node, stop_node):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and stop_node, using bfs determine if there is a path between the two nodes. If
    there is a path return a list containing the names of the nodes that comprise the path
    in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    pass


def depth_first_search_by_criteria(g, start_node, stop_criteria):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and a function stop_criteria, using dfs determine if there is a path between the
    start_node and any node matching the stop_criteria. Nodes match the criteria if
    stop_criteria(node) == True

    If there is a path return a list containing the names of the nodes that
    comprise the path in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    pass
