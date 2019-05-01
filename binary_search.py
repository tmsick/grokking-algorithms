def binary_search(item, seq):
    low = 0
    high = len(seq)
    while high > low:
        i = (high + low) // 2
        guess = seq[i]
        if guess == item:
            return i
        elif guess > item:
            high = i
        else:
            low = i + 1
    return -1


def linear_search(item, seq):
    for i, guess in enumerate(seq):
        if guess == item:
            return i
    return -1


import random
max = 1 << 24
item = random.randrange(max)
seq = list(range(max))
idx = binary_search(item, seq)
print(item, idx)
