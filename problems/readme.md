# Solving Problems Using Graphs

This section contains practice problems for you to solve, using the graph interface you've implemented. Each problem will require you to implement a new algorithm, which will accept a Graph or DirectedGraph as input. I hope you'll find the problems fun, and engaging.

My recommendation is to attempt the problems in the following order, good luck!

## Word Ladder

A word ladder is a way to connect 2 words. If you can take a word, changing one letter at a time, turn it into another word, and every intermediate step is still a word, those two words have a word ladder. For example, a ladder can be built between cat and dog:

```
cat
cot
dot
dog
```

Three letter words are pretty easy, four letter words are harder.

Can you create an algorithm, using you graph library, that can determine if two words have a ladder; and if so return the series of words that makeup the word ladder, in order.

> This problem can be reduced to the shortest path problem, using an undirected, unweighted graph.

## Bushwhacking

You're going on an expedition -- there are no trails or roads where you're headed. The terrain is rough and rocky, and some of it is impassable. You have a rough map of the terrain, and you've sliced it up into a grid. For every square in the grid, you've assigned the terrain a difficulty rating from 1 to 10, and marked terrain that is impassable with a -1. Conveniently, you have scanned this data and created a CSV to match. Here is an example of such a CSV:

```
1,2,1,2,1;
1,4,3,-1,1;
1,4,4,-1,1;
1,2,5,2,1;
```

In this map, two squares are impassable and the best route is along the top, then the right side.

Can you design an algorithm that uses your graph interface to find optimal routes in such CSVs?

## Thrift Hunter

Thrifty shoppers are willing to go to more than one store for their groceries. Given a list of prices, one list from each store, and a shopping list, and the price of gas for driving between each store, determine which stores you should visit, and which goods you should buy from which store.

## WikiVisualize

Wikipedia is a directed graph. Instructors for how to read it into a graph format that supports good visualization options. We will use external tools for this.

## Traffic Jam

You've modeled your city's roads as a graph. Nodes are intersections, and edges are weighted with the number of cars that can pass through per minute. Your job is in event planning -- every so often an event occurs, drawing people to specific places in the city, preventing roads from being used by cars. Given a DirectedGraph, a list of sources, and a list of destinations, can you predict if your road system can handle the traffic?

## Genome Assembly

Describe genome assembly!
