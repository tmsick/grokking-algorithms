def construct_power_set(elements: list, trunk: list, flags=[], idx=0):
    if idx == len(elements):
        trunk.append({elements[i] for i, f in enumerate(flags) if f})
        return
    construct_power_set(elements, trunk, flags + [True], idx + 1)
    construct_power_set(elements, trunk, flags + [False], idx + 1)


elements = {'a', 'b', 'c'}
trunk = []
construct_power_set(list(elements), trunk)
print(trunk)
