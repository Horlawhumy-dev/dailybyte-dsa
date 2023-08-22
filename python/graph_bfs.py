

from collections import deque, defaultdict


graph = defaultdict()

graph['A'] = ['B', 'D']
graph['B'] = ['A', 'C', 'F']
graph['C'] = ['B', 'F']
graph['D'] = ['A', 'F']
graph['F'] = ['B', 'C', 'D']


def graph_bfs(graph, root):
    """
        T(C) => O(V+E)
        S(C) => O(V)
    """
    visted_vertices = list()

    graph_queue = deque([root])

    visted_vertices.append(root)

    node = root

    while len(graph_queue) > 0:

        node = graph_queue.popleft()

        adjacent_vertices = graph[node] #vertices of node from graph

        remaining_vertices = set(adjacent_vertices).difference(set(visted_vertices)) #returns elements left in adj list

        if len(remaining_vertices) > 0:

            for vertice in sorted(remaining_vertices):
                visted_vertices.append(vertice)
                graph_queue.append(vertice) 


    return visted_vertices

print(graph_bfs(graph, 'A'))