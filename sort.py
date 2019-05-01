def bubble_sort(seq):
    seq = seq[:]
    for i in range(0, len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq


def selection_sort(seq):
    def get_smallest_index(seq):
        idx = 0
        smallest = seq[idx]
        for i in range(idx + 1, len(seq)):
            if seq[i] < smallest:
                smallest = seq[i]
                idx = i
        return idx

    seq = seq[:]
    sorted = []
    while len(seq) > 0:
        i = get_smallest_index(seq)
        sorted.append(seq.pop(i))
    return sorted


my_list = list(range(10, 0, -1))
print(bubble_sort(my_list))
print(selection_sort(my_list))
print(my_list)
