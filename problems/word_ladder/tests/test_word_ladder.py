from problems.word_ladder import reference_implementation as wl

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


def test_solve_word_ladder():
    dictionary = [
        'cat',
        'cot',
        'dot',
        'dog',
        'can',
        'cop',
        'pop'
    ]

    sol = wl.solve_word_ladder(dictionary, 'cat', 'dog')
    assert sol == ['cat', 'cot', 'dot', 'dog']

    sol = wl.solve_word_ladder(dictionary, 'cat', 'pop')
    assert sol == ['cat', 'cot', 'cop', 'pop']

    sol = wl.solve_word_ladder(dictionary, 'cat', 'can')
    assert sol == ['cat', 'can']

    sol = wl.solve_word_ladder(dictionary, 'cat', 'cat')
    assert sol == ['cat']

    sol = wl.solve_word_ladder(dictionary, 'cat', 'car') # Because car isn't in OUR dictionary, although it is a word
    assert sol is None


def test_lazy_word_ladder():
    pass
