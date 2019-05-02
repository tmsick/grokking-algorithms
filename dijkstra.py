edges = {(0, 1, 6), (0, 2, 2), (1, 3, 1), (2, 1, 3), (2, 3, 5)}
nodes = {e[0] for e in edges} | {e[1] for e in edges}
table = {n: float('inf') for n in nodes}

first = 0
table[first] = 0
pivot_node = first

while len(nodes) > 1:
    pivot_edges = {e for e in edges if e[0] == pivot_node}
    for pivot_edge in pivot_edges:
        table[pivot_edge[1]] = min((
            table[pivot_edge[0]] + pivot_edge[2],
            table[pivot_edge[1]],
        ))
    nodes.remove(pivot_node)
    pivot_node = min(nodes, key=lambda n: table[n])

print(table)
