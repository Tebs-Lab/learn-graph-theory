# Feel free to define any helper functions, or import anything from this repo or
# the standard library


def construct_three_jugs_graph():
    '''
    This function constructs and returns a DirectedGraph representing the
    three jugs problem. Each node in the graph is represented by a 3-tuple
    where the three values represent the amount of water currently in each jug,
    (twelve_liter, eight_liter, five_liter).

    The starting node is (12, 0, 0) -- 12 in the 12 liter, 0 in the 8 liter, and
    0 in the 5 liter. Creating the graph is essentially a depth first search
    algorithm over the space, but instead of stopping when we find a partiucular
    node, we explore until the frontier is empty.
    '''
    pass


def find_three_jugs_solution():
    '''
    Return a series of nodes that represents a solution to the three jugs problem.
    Because we're not looking for one specific node, but any node where a
    '''
    pass
