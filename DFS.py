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