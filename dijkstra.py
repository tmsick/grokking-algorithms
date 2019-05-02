edges = {
    ('piano book', 'poster', 0),
    ('piano book', 'lp', 5),
    ('poster', 'guitar base', 30),
    ('poster', 'drum set', 35),
    ('lp', 'guitar base', 15),
    ('lp', 'drum set', 20),
    ('guitar base', 'piano', 20),
    ('drum set', 'piano', 10),
}
nodes = {e[0] for e in edges} | {e[1] for e in edges}
table = {n: float('inf') for n in nodes}

first = 'piano book'
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
