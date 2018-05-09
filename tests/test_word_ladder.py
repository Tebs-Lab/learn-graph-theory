from problems.word_ladder import word_ladder as wl

def test_construct_word_ladder_graph():
    dictionary = [
        'cat',
        'cot',
        'dot',
        'dog'
    ]

    g = wl.construct_word_ladder_graph(dictionary)

    for word in dictionary:
        assert g.contains(word)

    edges = list(g.edges())
    assert len(edges) == 6
    assert ('cat', 'cot', 1) in edges
    assert ('cot', 'cat', 1) in edges
    assert ('cot', 'dot', 1) in edges
    assert ('dot', 'cot', 1) in edges
    assert ('dot', 'dog', 1) in edges
    assert ('dog', 'dot', 1) in edges


def test_shortest_path_bfs():
    dictionary = [
        'cat',
        'cot',
        'dot',
        'dog',
        'can',
        'cop',
        'pop'
    ]

    g = wl.construct_word_ladder_graph(dictionary)
    sol = wl.shortest_path_bfs(g, 'cat', 'dog')
    assert sol == ['cat', 'cot', 'dot', 'dog']

    sol = wl.shortest_path_bfs(g, 'cat', 'pop')
    assert sol == ['cat', 'cot', 'cop', 'pop']

    sol = wl.shortest_path_bfs(g, 'cat', 'can')
    assert sol == ['cat', 'can']

    sol = wl.shortest_path_bfs(g, 'cat', 'cat')
    assert sol == ['cat']

    sol = wl.shortest_path_bfs(g, 'cat', 'car') # Because car isn't in OUR dictionary, although it is a word
    assert sol is None


def test_lazy_word_ladder():
    pass
