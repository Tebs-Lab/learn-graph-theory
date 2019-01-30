from graphs.reference_implementation import DirectedGraph, UndirectedGraph
from algorithms.search.reference_implementation import depth_first_search

def test_start_is_stop():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'a') == ['a']


def test_no_path_directed():
    '''
    Test BFS on a simple directed graph that contains a no cycles, and no path to the goal.
    '''
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'e') is None


def test_no_path_directed_cycles():
    '''
    Test BFS on a simple directed graph that contains cycles, but no path to the goal.
    '''
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'e') is None


def test_single_path_directed():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'e') == ['a', 'b', 'd', 'e']


def test_multiple_paths_directed():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'e')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    found_path = depth_first_search(g, 'a', 'e')
    assert found_path == ['a', 'b', 'e'] or found_path == ['a', 'b', 'd', 'e']


def test_single_path_with_cycles_directed():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'h')
    g.add_edge('h', 'i')
    g.add_edge('i', 'j')
    g.add_edge('j', 'k')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')
    g.add_edge('f', 'b')

    assert depth_first_search(g, 'a', 'k') == ['a', 'b', 'c', 'h', 'i', 'j', 'k']


def test_no_path_undirected():
    '''
    Test BFS on a simple undirected graph that contains a no cycles, and no path to the goal.
    '''
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'e') is None


def test_no_path_undirected_cycles():
    '''
    Test BFS on a simple undirected graph that contains cycles, but no path to the goal.
    '''
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'e') is None


def test_single_path_undirected():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    assert depth_first_search(g, 'a', 'e') == ['a', 'b', 'd', 'e']


def test_multiple_paths_undirected():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'e')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')
    found_path = depth_first_search(g, 'a', 'e')

    assert found_path == ['a', 'b', 'e'] or found_path == ['a', 'b', 'd', 'e']


def test_single_path_with_cycles_undirected():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'h')
    g.add_edge('h', 'i')
    g.add_edge('i', 'j')
    g.add_edge('j', 'k')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')
    g.add_edge('f', 'b')

    assert depth_first_search(g, 'a', 'k') == ['a', 'b', 'c', 'h', 'i', 'j', 'k']
