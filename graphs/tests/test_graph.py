from graphs.reference_solutions import UndirectedGraph

# TODO: Extend tests, add directed graphs and student implementations

def test_create_graph_basic():
    '''
    test the basic creation api, along a happy path
    '''
    g = UndirectedGraph()

    assert g.add_node('a')
    assert g.add_node('b')
    assert g.add_node('c')

    # import ipdb; ipdb.set_trace()
    assert g.contains('a')
    assert g.contains('b')
    assert g.contains('c')

    nodes = list(g.nodes())
    assert 'a' in nodes
    assert 'b' in nodes
    assert 'c' in nodes

    g.add_edge('a', 'b')
    g.add_edge('a', 'c')

    edges = list(g.edges())
    assert len(edges) == 4 # "undirected" graph, must have edges both ways both times
    assert ('a', 'b', 1) in edges
    assert ('b', 'a', 1) in edges
    assert ('a', 'c', 1) in edges
    assert ('c', 'a', 1) in edges

    a_neigh = list(g.neighbors('a'))
    assert len(a_neigh) == 2
    assert ('b', 1) in a_neigh
    assert ('c', 1) in a_neigh

    b_neigh = list(g.neighbors('b'))
    assert len(b_neigh) == 1
    assert ('a', 1) in b_neigh

    c_neigh = list(g.neighbors('c'))
    assert len(c_neigh) == 1
    assert ('a', 1) in c_neigh
