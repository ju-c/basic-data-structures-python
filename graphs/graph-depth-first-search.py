from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def recursive_depth_first_search(graph, node, visited=None):

    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)

    unvisited = [n for n in graph[node] if n not in visited]

    for node in unvisited:
        recursive_depth_first_search(graph, node, visited)

    return visited


def iterative_depth_first_search(graph, node):

    visited = []
    stack = deque()
    stack.append(node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            stack.extend(unvisited)

    return visited


print(recursive_depth_first_search(graph, 'E'))
print(iterative_depth_first_search(graph, 'E'))
