from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def iterative_breadth_first_search(graph, start):

    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            unvisited = [n for n in graph[node] if n not in visited]
            queue.extend(unvisited)

    return visited


print(iterative_breadth_first_search(graph, 'A'))
