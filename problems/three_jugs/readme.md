# The Three Jugs Problem

You have 3 containers of different sizes. One holds 12 liters, one holds 8 liters, and the last holds 5 liters. The 12 liter container is full of liquid, the other two are empty. Using only the three containers and no other measuring tools, can you fill one of the containers with exactly 6 liters of liquid?

> This puzzle dates back to 1484 and a variant of it features in the plot of Die Hard 3.

Students are challenged to implement two functions, `construct_three_jugs_graph` and `find_three_jugs_solution` neither of which accept any input. Constructing the three jugs graph will require students to wrestle with the rules of pouring water from jug to jug (without spilling any), as well as model this problem as a graph.

Solving the puzzle will require students to apply search to the graph in order to find a series of actions that result in having 6 liters of water in any one jug.
