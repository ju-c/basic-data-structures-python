from collections import deque

graph = {
    'A': ['B', 'D', 'G'],
    'B': ['C'],
    'C': [],
    'D': ['B', 'F'],
    'E': ['D'],
    'F': [],
    'G': []
}

edges = [
    ['A', 'C'],
    ['A', 'B'],
    ['C', 'B'],
    ['C', 'D'],
    ['B', 'D'],
    ['E', 'D'],
    ['G', 'F']
]


def has_path_dfs(graph, start, destination):
    if start == destination:
        return True

    for adjacent_node in graph[start]:
        if has_path_dfs(graph, adjacent_node, destination) is True:
            return True

    return False


def has_path_bfs(graph, start, destination):
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == destination:
            return True

        for adjacent_node in graph[current]:
            queue.append(adjacent_node)

    return False


def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1
        return count


def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for adjacent_node in graph[current]:
        explore(graph, adjacent_node, visited)

    return True


def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = exploring_size(graph, node, visited)
        if size > largest:
            largest = size
    return largest


def exploring_size(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)
    size = 1

    for adjacent_node in graph[node]:
        size += exploring_size(graph, adjacent_node, visited)

    return size


def shortest_path(edges, start, destination):
    graph = building_graph(edges)
    visited = set([start])
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == destination:
            return distance

        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                queue.append((adjacent_node, distance + 1))

    return -1


def building_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in edges:
            graph[a] = []
        if b not in edges:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


print(has_path_dfs(graph, 'A', 'F'))
print(has_path_bfs(graph, 'A', 'F'))
print(connected_components_count(graph))
print(largest_component(graph))
print(shortest_path(edges, 'E', 'C'))
