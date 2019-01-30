from graphs.reference_implementation import DirectedGraph
from algorithms.search.reference_implementation import breadth_first_search_by_criteria

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
    g = DirectedGraph()

    frontier = []
    explored = set()

    # The start node
    frontier.append((12, 0, 0))

    while len(frontier) > 0:
        current_state = frontier.pop()

        if current_state in explored:
            continue

        g.add_node(current_state)

        # Discover nodes and edges for the neighbors
        twelve_amount, eight_amount, five_amount = current_state
        if twelve_amount > 0:
            # Pouring 12 into 8
            if eight_amount < 8:
                amount_poured = min((8 - eight_amount), twelve_amount)
                next_state = (twelve_amount - amount_poured, eight_amount + amount_poured, five_amount)
                g.add_node(next_state)
                g.add_edge(current_state, next_state)
                frontier.append(next_state)

            # Pouring 12 into 5
            if five_amount < 5:
                amount_poured = min((5 - five_amount), twelve_amount)
                next_state = (twelve_amount - amount_poured, eight_amount, five_amount + amount_poured)
                g.add_node(next_state)
                g.add_edge(current_state, next_state)
                frontier.append(next_state)

        if eight_amount > 0:
            # Pouring 8 into 12
            if twelve_amount < 12:
                amount_poured = min((12 - twelve_amount), eight_amount)
                next_state = (twelve_amount + amount_poured, eight_amount - amount_poured, five_amount)
                g.add_node(next_state)
                g.add_edge(current_state, next_state)
                frontier.append(next_state)

            # Pouring 8 into 5
            if five_amount < 5:
                amount_poured = min((5 - five_amount), eight_amount)
                next_state = (twelve_amount, eight_amount - amount_poured, five_amount + amount_poured)
                g.add_node(next_state)
                g.add_edge(current_state, next_state)
                frontier.append(next_state)

        if five_amount > 0:
            # Pouring 5 into 12
            if twelve_amount < 12:
                amount_poured = min((12 - twelve_amount), five_amount)
                next_state = (twelve_amount + amount_poured, eight_amount, five_amount - amount_poured)
                g.add_node(next_state)
                g.add_edge(current_state, next_state)
                frontier.append(next_state)

            # Pouring 5 into 8
            if eight_amount < 8:
                amount_poured = min((8 - eight_amount), five_amount)
                next_state = (twelve_amount, eight_amount + amount_poured, five_amount - amount_poured)
                g.add_node(next_state)
                g.add_edge(current_state, next_state)
                frontier.append(next_state)

        explored.add(current_state)

    return g


def find_three_jugs_solution():
    '''
    Return a series of nodes that represents a solution to the three jugs problem.
    '''
    g = construct_three_jugs_graph()
    def stop_criteria(node):
        return node[0] == 6 or node[1] == 6

    return breadth_first_search_by_criteria(g, (12, 0, 0), stop_criteria)
