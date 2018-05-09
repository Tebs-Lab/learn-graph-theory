# Word Ladders

A word ladder is a way to connect 2 words. If you can take a word, changing one letter at a time, turn it into another word, and every intermediate step is still a word, those two words have a word ladder. For example, a ladder can be built between cat and dog:

```
cat
cot
dot
dog
```

In this exercise we will be using the graph library we built in order to determine if two words have a ladder; and if so return the series of words that makeup the word ladder.

## Connection To Graph Theory

The first step in solving any problem with using graph theory is to model the problem as a graph. This always involves answering the same questions:

* What are the nodes, what are the things that have relationships?
* What are the edges, how should we codify the relationships that exist?
* What kind of edges should we use?
  * Weighted or unweighted, are the relationships all the same or do they have differing relative values?
  * Labeled edges, are all the relationships of the same type, or are there multiple kinds of relationships?
  * Directed or undirected, are all relationships mutual, or are some relationships one way?
* Finally, what part of graph theory answers the question we have, now that we've modeled our information as a graph?
  * Is this a shortest path, minimum spanning tree, max flow, or some other kind of problem?
  * Do I have to define other things, based on my choice? For example,
    * If I think this is a shortest path problem, what are the start and end nodes?
    * If I think this is a max flow problem, what are the source and sink nodes?

Take 10 minutes before continuing, and try to answer these questions for the Word Ladder problem described above. My answers to these questions are below -- but don't rob yourself of the chance to practice by skipping ahead!

__ADD SOME KIND OF SPACER__

## Word Ladders As Graphs

I like to model the word ladder problem as an unweighted, undirected, unlabeled graph. This is why I chose word ladder as the first problem for the series.

* What are the nodes?
  * Each node represents a word.
* What are the edges?
  * Edges exist between nodes if:
    * The words are the same length, and
    * The words differ by exactly one letter at a particular index.
* Edge properties:
  * Undirected -- if I can move from cat to cot, I can move from cot to cat.
  * Unweighted -- no matter what letters are different or what position the letters are in, an edge still just takes us one step towards a solution.
  * Unlabeled -- every edge encodes the same information, described above.
* What part of graph theory should I use?
  * Any path, therefore I can use breadth first search, or depth first search.
  * If I wanted to find the shortest word ladder, I would have to use BFS.
    * Which I do, so I will!

This really an any path problem because, using the graph model described above, traveling from one node to the next changes exactly one letter of the word. If you can find a path from word A to word B changing one letter at a time, that's the definition of a word ladder. Additionally, we'll need a "dictionary" in the English language sense of the word to construct our graph.

## Programming It

In `word_ladder.py` you'll find two functions: `shortest_path_bfs` and `construct_word_graph`. Your job is to implement these two functions. `shortest_path_bfs` should take in a graph object, and the names of two nodes in the graph. This method should be completely abstract -- meaning, it should work for our graph class regardless of what the graph represents. The `construct_word_ladder_graph` function is our domain specific function -- this function accepts a list of words (the dictionary) and constructs a graph that we can use to solve the word ladder problem.

## Bonus Work, Stretch It

It's also possible to write an algorithm based on BFS that creates the graph "lazily". In many cases this tactic will be faster. It entails using graph theory without actually building a graph data structure. This strategy can be faster and more space efficient because the whole graph we build may contain significantly more nodes than we need to explore in finding the word ladder. Combining the features of `construct_word_graph` and `shortest_path_bfs` into a single function, which I've called `lazy_word_ladder` can help you apply graph theory without exhaustively building a large graph and without actually building an explicit "graph" interface. All you need is a frontier and an explored list.
