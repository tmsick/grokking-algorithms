graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = float('inf')

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = set()


def find_lower_cost_node(costs):
    unprocessed = set(costs) - processed
    if len(unprocessed) == 0:
        return None
    return min(unprocessed, key=lambda k: costs[k])


# get the first node and make it the pivot node
node = find_lower_cost_node(costs)

while node is not None:
    # get the cost of the pivot node itself
    cost = costs[node]
    # retrieve the neighbors of the pivot node
    neighbors = graph[node]
    # for each neighbor...
    for n in neighbors:
        # calculate the cost of a neighbor based on the cost of the pivot node
        # and the weight on the edge between the pivot node and the neighbor
        new_cost = cost + neighbors[n]
        # if the newly calculated cost of the neighbor is less than the current
        # cost...
        if costs[n] > new_cost:
            # overwrite the cost with the lesser
            costs[n] = new_cost
            # overwrite the parent of the neighbor with the pivot node
            parents[n] = node
    # mark the pivot node processed
    processed.add(node)
    # get the next node
    node = find_lower_cost_node(costs)

print(costs)
