from graphs.reference_solutions import UndirectedGraph
from algorithms.search.reference_implementation import breadth_first_search

def construct_word_ladder_graph(word_list):
    '''
    Given a list of words (all of which are assumed to be the same length) construct
    a graph that can be used to solve the word_ladder_problem. Specifically your
    graph should have a single node for every word in the word list, and an edge that
    connects nodes if the two words are different by exactly one letter.
    '''
    g = UndirectedGraph()
    for w_idx, word in enumerate(word_list):
        for other in word_list[w_idx:]:
            assert len(word) == len(other)
            differences = 0
            for i in range(len(word)):
                if word[i] != other[i]:
                    differences += 1
                if differences > 1:
                    break

            if differences == 1:
                g.add_edge(word, other)

    return g


def solve_word_ladder(word_list, start_word, stop_word):
    '''
    Given a list of allowed words (word_list), a start_word, and a stop_node
    determine if the words can be laddered. If so, return that ladder, if not
    return None.
    '''
    g = construct_word_ladder_graph(word_list)
    ladder = breadth_first_search(g, start_word, stop_word)
    return ladder


def lazy_word_ladder(word_list, start_word, stop_word):
    '''
    Given a word list, start_word, and stop_word, determine if word_lists contains
    a ladder from start_word to stop_word. If it does, return the words in the ladder.
    If it does not, return None. If the start_word is the stop_word, return [start_word]

    This function should not build a graph from the entierty of word_list -- instead it
    should explore words one at a time, therefore expanding the fewest possible number
    of nodes between start_word and stop_word.
    '''
    pass
