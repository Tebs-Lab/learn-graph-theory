import os
from problems.word_ladder import reference_implementation as wl

def test_construct_word_ladder_graph_1():
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

def test_construct_word_ladder_graph_2():
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

    for word in dictionary:
        assert g.contains(word)

    edges = list(g.edges())
    assert len(edges) == 12
    assert ('cat', 'cot', 1) in edges
    assert ('cot', 'cat', 1) in edges
    assert ('cat', 'can', 1) in edges
    assert ('can', 'cat', 1) in edges
    assert ('cot', 'dot', 1) in edges
    assert ('dot', 'cot', 1) in edges
    assert ('cot', 'cop', 1) in edges
    assert ('cop', 'cot', 1) in edges
    assert ('cop', 'pop', 1) in edges
    assert ('pop', 'cop', 1) in edges
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

    g = wl.construct_word_ladder_graph(dictionary)
    sol = wl.solve_word_ladder(g, 'cat', 'dog')
    assert sol == ['cat', 'cot', 'dot', 'dog']

    sol = wl.solve_word_ladder(g, 'cat', 'pop')
    assert sol == ['cat', 'cot', 'cop', 'pop']

    sol = wl.solve_word_ladder(g, 'cat', 'can')
    assert sol == ['cat', 'can']

    sol = wl.solve_word_ladder(g, 'cat', 'cat')
    assert sol == ['cat']

    sol = wl.solve_word_ladder(g, 'cat', 'car') # Because car isn't in OUR dictionary, although it is a word
    assert sol is None


def test_five_letter_large():
    file_path = os.path.join(os.path.dirname(__file__), 'five_letter_dictionary.txt')
    f = open(file_path, 'r+')
    dictionary = [line.strip() for line in f.readlines()]
    g = wl.construct_word_ladder_graph(dictionary)

    # There are potentially many different solutions to these
    # but in our five_letter_dictionary there ARE solutions for
    # all of them. Our test does not test for a particular solution,
    # only that each word is a member of the dictionary, and that
    # words in the path differ by exactly 1 letter each step.
    bride_and_groom = wl.solve_word_ladder(g, 'bride', 'groom')
    for word in bride_and_groom:
        assert word in dictionary

    assert _is_valid_ladder(bride_and_groom)

    fresh_to_stale = wl.solve_word_ladder(g, 'fresh', 'stale')
    for word in fresh_to_stale:
        assert word in dictionary

    assert _is_valid_ladder(fresh_to_stale)

    a_to_z =  wl.solve_word_ladder(g, 'aahed', 'zymes')
    for word in a_to_z:
        assert word in dictionary

    assert _is_valid_ladder(a_to_z)


def _is_valid_ladder(word_list):
    for idx, word in enumerate(word_list[:-1]):
        if not _differ_by_exactly_one_letter(word, word_list[idx+1]):
            return False

    return True


def _differ_by_exactly_one_letter(word_a, word_b):
    if len(word_a) != len(word_b):
        return False
    differences = 0
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            differences += 1
        if differences > 1:
            break

    if differences == 1:
        return True

    return False
