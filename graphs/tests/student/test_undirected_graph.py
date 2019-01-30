from graphs.student_implementation import UndirectedGraph


def test_add_contains():
    '''
    Adding a node should cause contains to return true, adding a duplicate
    should return False, and contains should still report True for that node
    '''
    g = UndirectedGraph()
    assert g.add_node('a')
    assert g.contains('a')
    assert g.add_node('a') == False
    assert g.contains('a')

def test_add_nodes():
    '''
    Adding a node should cause that node to appear in the return value of .nodes().
    '''
    g = UndirectedGraph()
    assert g.add_node('a')
    assert 'a' in g.nodes()
    assert len(list(g.nodes())) == 1

    assert g.add_node('a') == False
    assert 'a' in g.nodes()
    assert len(list(g.nodes())) == 1

    assert g.add_node('b')
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert len(list(g.nodes())) == 2


def test_add_edge_neighbors():
    '''
    add_edge should connect existing nodes in the graph, causing neighbors to
    return the connected edges.

    add_edge should not overwrite existing edges and return False if the user tries.

    add_edge should create nodes if they do not already exist.
    '''
    g = UndirectedGraph()

    # Edges can connect existing nodes
    assert g.add_node('a')
    assert g.add_node('b')
    assert g.add_edge('a', 'b') # Default weight is 1
    assert ('b', 1) in g.neighbors('a')
    assert ('a', 1) in g.neighbors('b')

    # Adding an edge that already exists should be rejected, and return False
    assert g.add_edge('a', 'b', 2) == False
    assert ('b', 1) in g.neighbors('a')
    assert ('a', 1) in g.neighbors('b')

    # Adding an edge with a non-existing node works just fine
    assert g.add_edge('b', 'c', 2)
    assert ('b', 1) in g.neighbors('a')
    assert ('a', 1) in g.neighbors('b')
    assert ('c', 2) in g.neighbors('b')
    assert ('b', 2) in g.neighbors('c')


def test_add_edge_edges():
    '''
    add_edge should connect existing nodes in the graph, causing neighbors to
    return the connected edges.

    add_edge should not overwrite existing edges and return False if the user tries.

    add_edge should create nodes if they do not already exist.
    '''
    g = UndirectedGraph()

    # Edges can connect existing nodes
    assert g.add_node('a')
    assert g.add_node('b')
    assert g.add_edge('a', 'b')
    assert len(list(g.edges())) == 2
    assert ('a', 'b', 1) in g.edges()
    assert ('b', 'a', 1) in g.edges()

    # Adding an edge that already exists should be rejected, and return False
    assert g.add_edge('a', 'b', 2) == False
    assert len(list(g.edges())) == 2
    assert ('a', 'b', 1) in g.edges()
    assert ('b', 'a', 1) in g.edges()

    # Adding an edge with a non-existing node works just fine
    assert g.add_edge('b', 'c', 2)
    assert len(list(g.edges())) == 4
    assert ('a', 'b', 1) in g.edges()
    assert ('b', 'a', 1) in g.edges()
    assert ('b', 'c', 2) in g.edges()
    assert ('c', 'b', 2) in g.edges()


def test_add_edge_contains():
    '''
    Adding an edge between non-existant edges should cause contains to report they
    exist.
    '''
    g = UndirectedGraph()
    assert g.add_edge('a', 'b', 42)
    assert g.contains('a')
    assert g.contains('b')


def test_add_edge_nodes():
    '''
    Adding an edge between non-existant edges should cause those nodes to be
    returned by .nodes().
    '''
    g = UndirectedGraph()
    assert g.add_edge('a', 'b', 42)
    assert len(list(g.nodes())) == 2
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()


def test_simple_integration():
    '''
    test a simple use case, retesting assumptions at each step.
    '''
    g = UndirectedGraph()

    assert g.add_node('a')
    assert g.contains('a')
    assert len(list(g.nodes())) == 1
    assert 'a' in g.nodes()
    assert len(list(g.neighbors('a'))) == 0

    assert g.add_node('b')
    assert g.contains('b')
    assert len(list(g.nodes())) == 2
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert len(list(g.neighbors('a'))) == 0
    assert len(list(g.neighbors('b'))) == 0

    assert g.add_node('c')
    assert g.contains('c')
    assert len(list(g.nodes())) == 3
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert 'c' in g.nodes()
    assert len(list(g.neighbors('a'))) == 0
    assert len(list(g.neighbors('b'))) == 0
    assert len(list(g.neighbors('c'))) == 0

    g.add_edge('a', 'b')
    edges = list(g.edges())
    assert len(edges) == 2
    assert ('a', 'b', 1) in edges
    assert ('b', 'a', 1) in edges
    assert g.contains('a')
    assert g.contains('b')
    assert g.contains('c')
    assert len(list(g.nodes())) == 3
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert 'c' in g.nodes()
    assert len(list(g.neighbors('a'))) == 1
    assert ('b', 1) in g.neighbors('a')
    assert len(list(g.neighbors('b'))) == 1
    assert ('a', 1) in g.neighbors('b')
    assert len(list(g.neighbors('c'))) == 0

    g.add_edge('a', 'c')
    edges = list(g.edges())
    assert len(edges) == 4
    assert ('a', 'b', 1) in edges
    assert ('b', 'a', 1) in edges
    assert ('a', 'c', 1) in edges
    assert ('c', 'a', 1) in edges
    assert g.contains('a')
    assert g.contains('b')
    assert g.contains('c')
    assert len(list(g.nodes())) == 3
    assert 'a' in g.nodes()
    assert 'b' in g.nodes()
    assert 'c' in g.nodes()
    assert len(list(g.neighbors('a'))) == 2
    assert ('b', 1) in g.neighbors('a')
    assert ('c', 1) in g.neighbors('a')
    assert len(list(g.neighbors('b'))) == 1
    assert ('a', 1) in g.neighbors('b')
    assert len(list(g.neighbors('c'))) == 1
    assert ('a', 1) in g.neighbors('c')

    edges = list(g.edges())
    assert ('a', 'b', 1) in edges
    assert ('b', 'a', 1) in edges
    assert ('a', 'c', 1) in edges
    assert ('c', 'a', 1) in edges
