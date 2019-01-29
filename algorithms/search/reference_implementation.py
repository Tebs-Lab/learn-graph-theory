from collections import deque, namedtuple

# QueueItems helps with readability. In order to appropriately track the
# parent of each node as we explore the frontier, we need both these values in
# the frontier itself.
QueueItem = namedtuple('QueueItem', ('node', 'parent_node', 'cost'))

def breadth_first_search(g, start_node, stop_node):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and stop_node, using bfs determine if there is a path between the two nodes. If
    there is a path return a list containing the names of the nodes that comprise the path
    in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    frontier = deque() # We use appendLeft and pop so this behaves as a queue
    frontier.appendleft(QueueItem(start_node, None, 0))

    explored_list = {} # We point node_name to parent_node_name, so that we can get the path later
    explored_list[start_node] = None

    while len(frontier) > 0:
        current_node, parent_node, cost = frontier.pop()

        if current_node == stop_node:
            explored_list[current_node] = parent_node
            return _get_path_from_explored(explored_list, start_node, stop_node)

        # We could ignore weight for BFS, and in a high performance setting we probably would.
        for neighbor, weight in g.neighbors(current_node):
            if neighbor not in explored_list:
                frontier.appendleft(QueueItem(neighbor, current_node, cost + weight))

        explored_list[current_node] = parent_node

    return None


def breadth_first_search_by_criteria(g, start_node, stop_criteria):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and a function stop_criteria, using bfs determine if there is a path between the
    start_node and any node matching the stop_criteria. Nodes match the criteria if
    stop_criteria(node) == True

    If there is a path return a list containing the names of the nodes that
    comprise the path in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    frontier = deque() # We use appendLeft and pop so this behaves as a queue
    frontier.appendleft(QueueItem(start_node, None, 0))

    explored_list = {} # We point node_name to parent_node_name, so that we can get the path later
    explored_list[start_node] = None

    while len(frontier) > 0:
        current_node, parent_node, cost = frontier.pop()

        if stop_criteria(current_node) == True:
            explored_list[current_node] = parent_node
            return _get_path_from_explored(explored_list, start_node, current_node)

        # We could ignore weight for BFS, and in a high performance setting we probably would.
        for neighbor, weight in g.neighbors(current_node):
            if neighbor not in explored_list:
                frontier.appendleft(QueueItem(neighbor, current_node, cost + weight))

        explored_list[current_node] = parent_node

    return None

def depth_first_search(g, start_node, stop_node):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and stop_node, using bfs determine if there is a path between the two nodes. If
    there is a path return a list containing the names of the nodes that comprise the path
    in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    frontier = deque() # We use append and pop so this behaves as a stack
    frontier.append(QueueItem(start_node, None, 0))

    explored_list = {} # We point node_name to parent_node_name, so that we can get the path later
    explored_list[start_node] = None

    while len(frontier) > 0:
        current_node, parent_node, cost = frontier.pop()

        if current_node == stop_node:
            explored_list[current_node] = parent_node
            return _get_path_from_explored(explored_list, start_node, stop_node)

        # We could ignore weight for BFS, and in a high performance setting we probably would.
        for neighbor, weight in g.neighbors(current_node):
            if neighbor not in explored_list:
                frontier.append(QueueItem(neighbor, current_node, cost + weight))

        explored_list[current_node] = parent_node

    return None


def depth_first_search_by_criteria(g, start_node, stop_criteria):
    '''
    Given a graph g, and the identifiers for two of the nodes in the graph, start_node
    and a function stop_criteria, using dfs determine if there is a path between the
    start_node and any node matching the stop_criteria. Nodes match the criteria if
    stop_criteria(node) == True

    If there is a path return a list containing the names of the nodes that
    comprise the path in the order that they will be reached from start to finish.

    If there is no path, return None.

    If the start_node is the stop_node, return [start_node]
    '''
    frontier = deque() # We use append and pop so this behaves as a stack
    frontier.append(QueueItem(start_node, None, 0))

    explored_list = {} # We point node_name to parent_node_name, so that we can get the path later
    explored_list[start_node] = None

    while len(frontier) > 0:
        current_node, parent_node, cost = frontier.pop()

        if stop_criteria(current_node) == True:
            explored_list[current_node] = parent_node
            return _get_path_from_explored(explored_list, start_node, current_node)

        # We could ignore weight for BFS, and in a high performance setting we probably would.
        for neighbor, weight in g.neighbors(current_node):
            if neighbor not in explored_list:
                frontier.append(QueueItem(neighbor, current_node, cost + weight))

        explored_list[current_node] = parent_node

    return None


def _get_path_from_explored(explored_list, start_node, stop_node):
    '''
    Simple helper that walks backwards from the stop_node to the start_node given
    an explored_list from one of the above search algorithms. The explored list
    must be a map of nodes to nodes such that explored_list[node_a] returns the
    node that node_a was reached from during search.
    '''
    path = [stop_node]
    while path[-1] != start_node:
        path.append(explored_list[path[-1]])
    path.reverse()
    return path
