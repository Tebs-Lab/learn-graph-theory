# Graph Theory Fundamentals Reference

This repository is associated with the [graph theory fundamentals series](). Everything in this repository has been released to the public domain without liability — you are free to copy, alter, remix, redistribute, and extend these materials for any purpose whatsoever.  These educational materials have been built to serve three purposes:

1. Provide clear, understandable, reference implementations of graph theory concepts and algorithms targeted at people learning these concepts for the first time.
1. Create opportunities for learners to practice implementing important graph theory concepts.
1. Provide a useful scaffold for educators and instructors to use in their own class materials.

## Getting Started

Because this repo is targeting students we have endeavored to favor simplicity and reduced reliance on third party code over speed, efficiency, and other priorities. However, we do think a sensible workflow and framework for expansion will serve the repo as time goes on. The code is packaged using [`pipenv`](https://pipenv.readthedocs.io/en/latest/) and has a single dependency: [`pytest`](https://docs.pytest.org/en/latest/) which we personally find more friendly than Python's builtin UnitTest framework.

To install pipenv [follow the instructions here](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).

Then install the dependencies in a pipenv virtual environment navigate to the repo's root directory and run:

```
pipenv install
```

To quickly test if your installation worked run the tests from the same location:

```
pipenv run pytest
```

NOTE TO SELF: Some of the tests are going to be failing since they're for uncompleted exercises, note this here for people!

While working on the exercises, or exploring the rest of the repo, we recommend you do so within the context of the pipenv virtual environment, to activate it simply run the following in this repo's root directory:

```
pipenv shell
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

This approach also offers more for students and classes that might (very reasonably) want to stop at stage 1 or 2, training developers to trust and use API's. Our exercises rely on the reference implementations for everything except work related to the current problem in order to better support tackling this material in either order.

For students or instructors who want to follow the first (ground up) path, you may wish to change some of the import statements to rely on the student implementations rather than the provided reference implementations for each individual problem. Independence also makes it easier to implement some hybrid approach or do a single exercise a la carte.

## Advice For Using These Materials

In general, this repo is largely designed to track with the graph theory article series. Quickly scan this repository and take note of the work you'll be asked to do, essentially:

1. Implement a graph API
1. Implement search algorithms using a graph API
1. Solve the "3 jug problem"
1. Solve the "word ladder" problem

Our general advice is to read the articles, then attempt the work. When you feel like you've read enough to attempt one of these problems, come back here and practice! That said, for students who want a little more advice consider the following:

### Top Down Approach

The article series is ordered with this approach in mind. This approach might be preferable for students who have less experience with data structures and algorithms, or students who don't want to get all the way into the nuts and bolts of graph API implementation and would rather just gain insight into using an existing API.

Read through those articles and periodically come back to this repo to practice. After reading "modeling problems with graphs" attempt the word ladder and 3 jug problems from this repo.

If you feel stuck on those problems, read basic graph search and then revisit the problems. If you're still feeling stuck read through the 3 jug problem article and try again.

After solving the problems using one of the provided algorithms, read through the article about basic graph search and come back to implement DFS and BFS. Finally, read the article about implementing graphs and return here once again to implement them.

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
