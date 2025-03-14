# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-ttUWhZc6st4jgKII1XLP9aY2zUcEcbf
"""

# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-k3DJ5orcitK--ya4UK-ebzCF2uyzVJv
"""

# -*- coding: utf-8 -*-
"""BFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mPgJnrWJLoikY6fhR9lpjsLvAGi1W8cj
"""

import collections

# BFS algorithm
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + "", end=" ")
        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {'T': ['S', 'L'], 'S': ['L'], 'L': ['M'], 'M': ['S', 'L']}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 'T')

# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-k3DJ5orcitK--ya4UK-ebzCF2uyzVJv
"""

# -*- coding: utf-8 -*-
"""DFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mPgJnrWJLoikY6fhR9lpjsLvAGi1W8cj
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge('T', 'S')
    g.addEdge('T', 'L')
    g.addEdge('S', 'L')
    g.addEdge('L', 'T')
    g.addEdge('L', 'M')
    g.addEdge('M', 'M')

    print("Berikut adalah Penelusuran Depth First (dimulai dari node L)")
    g.DFS('L')

# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-k3DJ5orcitK--ya4UK-ebzCF2uyzVJv
"""

# -*- coding: utf-8 -*-
"""UCS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mPgJnrWJLoikY6fhR9lpjsLvAGi1W8cj
"""

import heapq

# Uniform Cost Search algorithm
def uniform_cost_search(goal, start):
    global graph, cost
    answer = [10**8] * len(goal)

    # Priority queue (min-heap)
    queue = []
    heapq.heappush(queue, (0, start))  # (cost, node)

    visited = set()
    count = 0

    while queue:
        p_cost, p_node = heapq.heappop(queue)

        if p_node in goal:
            index = goal.index(p_node)
            if answer[index] == 10**8:
                count += 1
            answer[index] = min(answer[index], p_cost)
            if count == len(goal):
                return answer

        if p_node not in visited:
            visited.add(p_node)
            for neighbor in graph[p_node]:
                edge_cost = cost.get((p_node, neighbor), float('inf'))
                heapq.heappush(queue, (p_cost + edge_cost, neighbor))

    return answer

if __name__ == '__main__':
    # Create graph
    graph = {
        "A": ["B", "D"], "B": ["G"], "D": ["B", "G", "E"],
        "C": ["B"], "E": ["C", "F", "G", "D"], "F": ["C", "G"], "G": ["E"]
    }
    cost = {
        ("A", "B"): 3, ("A", "D"): 6, ("B", "G"): 2, ("D", "B"): 4,
        ("D", "G"): 5, ("D", "E"): 3, ("C", "B"): 5, ("E", "C"): 4,
        ("E", "F"): 3, ("E", "G"): 5, ("E", "D"): 3, ("F", "C"): 7,
        ("F", "G"): 4, ("G", "E"): 6
    }

    # Goal state
    goal = ["G"]

    # Get the answer
    answer = uniform_cost_search(goal, "A")

    # Print result
    print("Minimum cost from A to G is =", answer[0])