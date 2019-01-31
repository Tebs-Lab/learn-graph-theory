# Graph Theory Fundamentals Reference

This repository is associated with the [graph theory fundamentals series](). Everything in this repository has been released to the public domain without liability — you are free to copy, alter, remix, redistribute, and extend these materials for any purpose whatsoever.  These educational materials have been built to serve three purposes:

1. Provide clear, understandable, reference implementations of graph theory concepts and algorithms targeted at people learning these concepts for the first time.
1. Create opportunities for learners to practice implementing important graph theory concepts and algorithms.
1. Provide a useful scaffold for educators and instructors to use in their own class materials.

## Getting Started

Because this repo is targeting students we have endeavored to favor simplicity over speed, efficiency, and other priorities. However, we do think a sensible workflow and framework for expansion will serve the repo as time goes on. The code is packaged using [`pipenv`](https://pipenv.readthedocs.io/en/latest/) and has a single dependency: [`pytest`](https://docs.pytest.org/en/latest/) which we personally find more friendly than Python's builtin UnitTest framework.

To install pipenv [follow the instructions here](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).

To install the dependency in a pipenv virtual environment, navigate to the repo's root directory and run:

```
pipenv install
```

While working on the exercises, or exploring the rest of the repo, we recommend you do so within the context of the pipenv virtual environment, to activate it simply run the following in this repo's root directory:

```
pipenv shell
```

If you do not activate your virtual environment using `pipenv shell` then you'll have to prefix any commands you wish to run with `pipenv run`. For example, to run the tests after running `pipenv install` you can either run:

```
pipenv run pytest

# or

pipenv shell
pytest
```

Running the tests with `pytest` will run the tests for both the reference implementations as well as the student stubs. As a result, you should see a mix of failures and successes:

```
 bash-3.2$ pytest
================================================ test session starts =================================================
platform darwin -- Python 3.6.5, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
rootdir: /Users/tylerbettilyon/side-projects/graph-theory-udemy, inifile:
collected 138 items                                                                                                  

algorithms/search/tests/reference/test_bfs.py .............                                                    [  9%]
algorithms/search/tests/reference/test_bfs_by_critera.py .............                                         [ 18%]
algorithms/search/tests/reference/test_dfs.py ...........                                                      [ 26%]
algorithms/search/tests/reference/test_dfs_by_critera.py ............                                          [ 35%]
algorithms/search/tests/student/test_bfs.py F..FFF..FFFFF                                                      [ 44%]
algorithms/search/tests/student/test_bfs_by_critera.py F..FFF..FFFFF                                           [ 54%]
algorithms/search/tests/student/test_dfs.py F..FFF..FFF                                                        [ 62%]
algorithms/search/tests/student/test_dfs_by_critera.py F..FFF..FFFF                                            [ 71%]
graphs/tests/reference/test_directed_graph.py .......                                                          [ 76%]
graphs/tests/reference/test_undirected_graph.py .......                                                        [ 81%]
graphs/tests/student/test_directed_graph.py FFFFFFF                                                            [ 86%]
graphs/tests/student/test_undirected_graph.py FFFFFFF                                                          [ 91%]
problems/three_jugs/tests/reference/test_three_jugs.py ..                                                      [ 92%]
problems/three_jugs/tests/student/test_three_jugs.py FF                                                        [ 94%]
problems/word_ladder/tests/reference/test_word_ladder.py ....                                                  [ 97%]
problems/word_ladder/tests/student/test_word_ladder.py FFFF    
```

If you'd like to test a specific component you can provide the path to that component:

```
pytest graphs/  # This will only run the tests under the graphs directory
```

If you'd like to test only the reference implementations, or only the student implementations you can use pytest's keyword flag:

```
pytest -k reference  # Will only test the reference implementations
pytest -k student  # Will only test the student implementations
```

And of course you can combine the two:

```
pytest -k student graphs  # Will only test the student implementations under the graph directory
```

## What's In this Repo?

There are two kinds of content in this repository: reference implementations of graph theory concepts and exercises for students to practice graph theory concepts. Every reference solution contains a partially complete source file intended for student implementation. These student implementation files have been scaffolded enough to conform to an API, for which tests are provided.

There are three folders:

`graphs` contains implementations of graph libraries.  
`algorithms` contains problem agnostic (general purpose) implementations of graph algorithms such as breadth first search and depth first search.  
`problems` contains descriptions of problems that can be solved using a combination of a graph implementation from `graphs` and a algorithm(s) from `algorithms`.

Each of these folders contains reference implementations and tests as well as a scaffolded source files for student work. Each exercise has been made as independent as possible from the other exercises. It's very tempting to take a "NAND to Tetris" style approach and ask students to build everything from the ground up:

1. Build a graph API implementation, then
1. Implement search against those implementations, then
1. Use a search implementation to solve problems...

You can absolutely approach these exercises in this way, and it will be great for some learners and some learning environments. However, we also think there is a lot of value to an approach that dives into the layers of abstraction in the opposite order:

1. First, use a well tested graph API and search implementation to solve a problem. Then, expand your understanding by
1. Implementing search from scratch against a well tested graph API. Then, expand your understanding by
1. Implementing a graph API from scratch.

This approach also offers more for students and classes that might want to stop at stage 1 or 2. Our exercises rely on the reference implementations for everything except work related to the current problem in order to better support tackling this material in either order. However, students are welcome to swap out the reference implementation for their own by changing the `import` statements. This will be necessary for those taking the 'ground up' approach.

## Advice For Using These Materials

In general, this repo is largely designed to track with the graph theory article series. Quickly scan this repository and take note of the work you'll be asked to do, essentially:

1. Implement a graph API
1. Implement search algorithms using a graph API
1. Solve the "3 jug problem"
1. Solve the "word ladder" problem

Our general advice is to take stock of the exercises then read the articles. As soon as you feel like you've read enough to attempt one of these exercises, come back here and make an attempt. Applying this advice in the context of the two approaches described above might look like:

### Top Down Approach

The article series is ordered with this approach in mind. This approach might be preferable for students who have less experience with data structures and algorithms, or students who don't want to get all the way into the nuts and bolts of graph API implementation and would rather just gain insight into using an existing API.

After reading "modeling problems with graphs" attempt the word ladder and 3 jug problems from this repo. If you feel stuck, read basic graph search and then revisit the problems. If you're still feeling stuck read through the 3 jug solution article and try again. After solving the problems using one of the provided algorithms, read through the article about basic graph search and come back to implement DFS and BFS. Finally, read the article about implementing graphs and return here once again to implement them.

### Bottom Up Approach

This approach is most appropriate for students who:

1. Already have some engineering experience.
1. Are already motivated to learn graph theory.
1. Enjoy lower level thinking, or are seeking to practice that skill.

This approach puts a primacy on understanding a tool before you use it. For learners taking this approach we suggest reading the first three articles:

1. Why Learn Graph Theory
1. What Is a Graph
1. Types of Graph

Then, skip ahead to article 7, "Implementations of Graphs", then come back here and implement a directed and undirected graph. Then read article 6, "Basic Graph Search" and return here to implement BFS and DFS. Finally, read modeling problems with graphs and attempt to solve the word ladder and 3 jug problem.

## Support The Creation Of These Materials

This repo is managed by [Teb's Lab](www.tebs-lab.com). You can support our work by signing up for our [Patreon account](www.patreon.com/tebslab).
