from collections import deque
from src.graph import Graph

def construct_word_ladder_graph(word_list):
    '''
    Given a list of words (all of which are assumed to be the same length) construct
    a graph that can be used to solve the word_ladder_problem. Specifically your
    graph should have a single node for every word in the word list, and an edge that
    connects nodes if the two words are different by exactly one letter.
    '''
    g = Graph()
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


def shortest_path_bfs(g, start_name, stop_name):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_name
    and stop_name, using bfs determine if there is a path between the two nodes. If
    there is a path return a list containing the names of the nodes that comprise the path
    in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_name is the stop_name, return [start_name]
    '''
    frontier = deque() # I'll use appendLeft and pop so this behaves as a queue
    frontier.appendleft(start_name)

    found = {} # I'll point node_name to parent_node_name, so that we can get the path later
    found[start_name] = None

    while len(frontier) > 0:
        current_node = frontier.pop()

        if current_node == stop_name:
            # Backtrace to find the path
            path = [stop_name]
            while path[-1] != start_name:
                path.append(found[path[-1]])
            path.reverse()
            return path

        # BFS ignores edge weight
        for neighbor, _ in g.neighbors(current_node):
            # For BFS, the first time we encounter a neighbor will determine it's parent in the path
            # This assumption will not be true in Dijkstra's algorithm though.
            if neighbor not in found:
                frontier.appendleft(neighbor)
                found[neighbor] = current_node

    return None


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
