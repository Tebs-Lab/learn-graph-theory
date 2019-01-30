from problems.three_jugs.student_implementation import construct_three_jugs_graph, find_three_jugs_solution

def test_construct_three_jugs_graph():
    '''
    There is only one correct version of this graph. It has 25 nodes, 94 edges,
    codified below. However, it can be built programatically.
    '''
    cannonical_nodes, cannonical_edges = _get_cannon()
    g = construct_three_jugs_graph()
    assert len(list(g.nodes())) == len(cannonical_nodes)
    for node in cannonical_nodes:
        assert node in g.nodes()

    assert len(list(g.edges())) == len(cannonical_edges)
    for edge in cannonical_edges:
        assert edge in g.edges()


def test_three_jug_solution():
    '''
    Since there are many ways to find a solution (infinte if you include cycles)
    this test only tests that a submitted solution is a series of tuples representing
    a valid path in the cannonical three jugs graph and that the start node is correct
    and the final node is one with 6 gallons in one of the jugs
    '''
    cannonical_nodes, cannonical_edges = _get_cannon()
    path = find_three_jugs_solution()
    assert path[0] == (12, 0, 0) # started at correct node
    assert path[-1][0] == 6 or path[-1][1] == 6 # finished in a node matching the critera

    for i, node in enumerate(path[:-1]):
        assert node in cannonical_nodes
        next_node = path[i+1]
        assert (node, next_node, 1) in cannonical_edges

def _get_cannon():
    cannonical_nodes = [(12, 0, 0),
        (4, 8, 0),
        (7, 0, 5),
        (0, 7, 5),
        (7, 5, 0),
        (2, 5, 5),
        (2, 8, 2),
        (0, 8, 4),
        (10, 0, 2),
        (4, 3, 5),
        (9, 3, 0),
        (9, 0, 3),
        (1, 8, 3),
        (1, 6, 5),
        (6, 6, 0),
        (6, 1, 5),
        (11, 1, 0),
        (11, 0, 1),
        (3, 8, 1),
        (3, 4, 5),
        (8, 4, 0),
        (8, 0, 4),
        (5, 7, 0),
        (5, 2, 5),
        (10, 2, 0)
    ]

    cannonical_edges = [
        ((12, 0, 0), (4, 8, 0), 1),
        ((12, 0, 0), (7, 0, 5), 1),
        ((4, 8, 0), (0, 8, 4), 1),
        ((4, 8, 0), (12, 0, 0), 1),
        ((4, 8, 0), (4, 3, 5), 1),
        ((7, 0, 5), (0, 7, 5), 1),
        ((7, 0, 5), (12, 0, 0), 1),
        ((7, 0, 5), (7, 5, 0), 1),
        ((0, 7, 5), (7, 0, 5), 1),
        ((0, 7, 5), (5, 7, 0), 1),
        ((0, 7, 5), (0, 8, 4), 1),
        ((7, 5, 0), (4, 8, 0), 1),
        ((7, 5, 0), (2, 5, 5), 1),
        ((7, 5, 0), (12, 0, 0), 1),
        ((7, 5, 0), (7, 0, 5), 1),
        ((2, 5, 5), (0, 7, 5), 1),
        ((2, 5, 5), (7, 0, 5), 1),
        ((2, 5, 5), (7, 5, 0), 1),
        ((2, 5, 5), (2, 8, 2), 1),
        ((2, 8, 2), (0, 8, 4), 1),
        ((2, 8, 2), (10, 0, 2), 1),
        ((2, 8, 2), (2, 5, 5), 1),
        ((2, 8, 2), (4, 8, 0), 1),
        ((0, 8, 4), (8, 0, 4), 1),
        ((0, 8, 4), (0, 7, 5), 1),
        ((0, 8, 4), (4, 8, 0), 1),
        ((10, 0, 2), (2, 8, 2), 1),
        ((10, 0, 2), (7, 0, 5), 1),
        ((10, 0, 2), (12, 0, 0), 1),
        ((10, 0, 2), (10, 2, 0), 1),
        ((4, 3, 5), (0, 7, 5), 1),
        ((4, 3, 5), (7, 0, 5), 1),
        ((4, 3, 5), (9, 3, 0), 1),
        ((4, 3, 5), (4, 8, 0), 1),
        ((9, 3, 0), (4, 8, 0), 1),
        ((9, 3, 0), (4, 3, 5), 1),
        ((9, 3, 0), (12, 0, 0), 1),
        ((9, 3, 0), (9, 0, 3), 1),
        ((9, 0, 3), (1, 8, 3), 1),
        ((9, 0, 3), (7, 0, 5), 1),
        ((9, 0, 3), (12, 0, 0), 1),
        ((9, 0, 3), (9, 3, 0), 1),
        ((1, 8, 3), (0, 8, 4), 1),
        ((1, 8, 3), (9, 0, 3), 1),
        ((1, 8, 3), (1, 6, 5), 1),
        ((1, 8, 3), (4, 8, 0), 1),
        ((1, 6, 5), (0, 7, 5), 1),
        ((1, 6, 5), (7, 0, 5), 1),
        ((1, 6, 5), (6, 6, 0), 1),
        ((1, 6, 5), (1, 8, 3), 1),
        ((6, 6, 0), (4, 8, 0), 1),
        ((6, 6, 0), (1, 6, 5), 1),
        ((6, 6, 0), (12, 0, 0), 1),
        ((6, 6, 0), (6, 1, 5), 1),
        ((6, 1, 5), (0, 7, 5), 1),
        ((6, 1, 5), (7, 0, 5), 1),
        ((6, 1, 5), (11, 1, 0), 1),
        ((6, 1, 5), (6, 6, 0), 1),
        ((11, 1, 0), (4, 8, 0), 1),
        ((11, 1, 0), (6, 1, 5), 1),
        ((11, 1, 0), (12, 0, 0), 1),
        ((11, 1, 0), (11, 0, 1), 1),
        ((11, 0, 1), (3, 8, 1), 1),
        ((11, 0, 1), (7, 0, 5), 1),
        ((11, 0, 1), (12, 0, 0), 1),
        ((11, 0, 1), (11, 1, 0), 1),
        ((3, 8, 1), (0, 8, 4), 1),
        ((3, 8, 1), (11, 0, 1), 1),
        ((3, 8, 1), (3, 4, 5), 1),
        ((3, 8, 1), (4, 8, 0), 1),
        ((3, 4, 5), (0, 7, 5), 1),
        ((3, 4, 5), (7, 0, 5), 1),
        ((3, 4, 5), (8, 4, 0), 1),
        ((3, 4, 5), (3, 8, 1), 1),
        ((8, 4, 0), (4, 8, 0), 1),
        ((8, 4, 0), (3, 4, 5), 1),
        ((8, 4, 0), (12, 0, 0), 1),
        ((8, 4, 0), (8, 0, 4), 1),
        ((8, 0, 4), (0, 8, 4), 1),
        ((8, 0, 4), (7, 0, 5), 1),
        ((8, 0, 4), (12, 0, 0), 1),
        ((8, 0, 4), (8, 4, 0), 1),
        ((5, 7, 0), (4, 8, 0), 1),
        ((5, 7, 0), (0, 7, 5), 1),
        ((5, 7, 0), (12, 0, 0), 1),
        ((5, 7, 0), (5, 2, 5), 1),
        ((5, 2, 5), (0, 7, 5), 1),
        ((5, 2, 5), (7, 0, 5), 1),
        ((5, 2, 5), (10, 2, 0), 1),
        ((5, 2, 5), (5, 7, 0), 1),
        ((10, 2, 0), (4, 8, 0), 1),
        ((10, 2, 0), (5, 2, 5), 1),
        ((10, 2, 0), (12, 0, 0), 1),
        ((10, 2, 0), (10, 0, 2), 1)
    ]

    return cannonical_nodes, cannonical_edges
