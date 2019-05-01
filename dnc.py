def my_sum(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + my_sum(seq[1:])


def binary_search_recursion(item, seq, offset=0):
    if len(seq) == 1:
        return offset
    mid = len(seq) // 2
    if seq[mid] > item:
        return binary_search_recursion(item, seq[:mid], offset)
    else:
        return binary_search_recursion(item, seq[mid:], offset + mid)


def quick_sort(seq):
    seq = seq[:]
    if len(seq) < 2:
        return seq
    pivot = seq.pop()
    lower = [i for i in seq if i <= pivot]
    higher = [i for i in seq if i > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(higher)


import random
seq = [random.randint(0, 99) for i in range(10)]
print(seq)
print(quick_sort(seq))
