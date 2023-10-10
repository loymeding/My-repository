def remove_edges(graph, x):
    edges_to_remove = []
    for node in graph:
        for edge in graph[node]:
            if edge[1] <= x:
                edges_to_remove.append((node, edge))

    for node, edge in edges_to_remove:
        graph[node].remove(edge)
    for node in graph.keys():
        graph[node].append([node, 0])


def count_connected_components(graph):
    visited = set()
    count = 0

    has_edge = False
    for vertex, edges in graph.items():
        for edge in edges:
            destination_vertex = edge[0]
            if destination_vertex == vertex:
                has_edge = True
                break
        if has_edge and len(list(graph.keys())) == 2:
            return 1

    def dfs(node):
        visited.add(node)
        for connection in graph[node]:
            if connection[0] not in visited:
                dfs(connection[0])

    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)

    return count


n, m = list(map(int, input().split()))
graph = {}
for i in range(1, n + 1):
    graph[i] = []

max_len = 0
for i in range(m):
    inp = list(map(int, input().split()))
    graph[inp[0]].append(inp[1:])
    road_len = inp[2]
    if road_len > max_len:
        max_len = road_len

num_components = count_connected_components(graph)
max_x = 0
for x in range(0, max_len):
    copy_graph = graph.copy()
    remove_edges(copy_graph, x)
    if count_connected_components(copy_graph) == num_components:
        max_x = x

print(max_x)
