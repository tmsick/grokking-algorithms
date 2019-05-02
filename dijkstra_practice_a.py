graph = {
    'A': {
        'neighbors': {
            'B': 5,
            'C': 2,
        },
        '__start__': True,
    },
    'B': {
        'neighbors': {
            'D': 4,
            'E': 2,
        },
    },
    'C': {
        'neighbors': {
            'B': 8,
            'E': 7,
        },
    },
    'D': {
        'neighbors': {
            'E': 6,
            'F': 3,
        },
    },
    'E': {
        'neighbors': {
            'F': 1,
        },
    },
    'F': {
        'neighbors': {},
        '__finish__': True,
    },
}

start = ''
finish = ''
for key, data in graph.items():
    if data.get('__start__'):
        start = key
    if data.get('__finish__'):
        finish = key

costs = {node: float('inf') for node in graph.keys()}
costs[start] = 0

parents = {node: None for node in graph.keys()}

processed = set()


def get_pivot_node(graph, costs, processed):
    unprocessed = set(graph) - processed
    if len(unprocessed) == 0:
        return None
    return min(unprocessed, key=lambda node: costs[node])


node = get_pivot_node(graph, costs, processed)
while node is not None:
    cost = costs[node]
    for nbr, weight in graph[node]['neighbors'].items():
        nbr_cost = cost + weight
        if nbr_cost < costs[nbr]:
            costs[nbr] = nbr_cost
            parents[nbr] = node
    processed.add(node)
    node = get_pivot_node(graph, costs, processed)

print(costs)
print(parents)
