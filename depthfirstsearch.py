# -*- coding: utf-8 -*-


def depth_first_search(graph, start, visited):
 visited.add(start)
 print(start)
 for neighbor in graph[start]:
    if neighbor not in visited:
      depth_first_search(graph,neighbor,visited)

graph = {
  'A': ['B', 'G'],
  'B': ['C', 'D', 'E'],
  'C': [],
  'D': [],
  'E': ['F'],
  'F': [],
  'G': ['H'],
  'H': ['I'],
  'I': []
}
visited = set()
depth_first_search(graph,"A",visited)
