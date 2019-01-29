# Search Algorithms

Search algorithms explore a graph in order to find paths between two nodes. There are currently two supported algorithms each in two styles. The two algorithms are BFS and DFS, and for each algorithm we support searching the graph for a specific node as well as searching for a node that matches some provided criteria.

For criteria matching, instead of specifying a node name users can provide a function or callable which accepts a node as input and returns True if the node should be considered a stopping node. This is especially useful for problems where there isn't a single solution node (such as the three jugs problem).
