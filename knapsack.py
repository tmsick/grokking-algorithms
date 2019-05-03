items = {
    'A': {
        'weight': 1,
        'value': 2,
    },
    'B': {
        'weight': 2,
        'value': 6,
    },
    'C': {
        'weight': 3,
        'value': 9,
    },
}


def dp(items, limit):
    grid = [[0 for j in range(limit + 1)] for i in range(len(items))]
    items_list = tuple(items)
    for i in range(len(grid)):
        items_available = {item for idx, item in enumerate(items) if idx <= i}
        for j in range(len(grid[0])):
            grid[i][j] = max({grid[i][j]} | {
                grid[i][j - items[item]['weight']] + items[item]['value']
                for item in items_available if j - items[item]['weight'] >= 0
            })
    return grid


result = dp(items, limit=5)
maximum = max({max(row) for row in result})
digits = len(str(maximum))
template = '%{}d'.format(digits)
for row in result:
    print(' '.join([template % i for i in row]))
