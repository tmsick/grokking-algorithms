graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def is_seller(name):
    return name.endswith('m')


def search(name):
    from collections import deque
    q = deque()
    q += graph[name]
    searched = set()
    while len(q) > 0:
        person = q.popleft()
        if person in searched:
            continue
        if is_seller(person):
            print(person + ' is a seller')
            return True
        print(person + ' is not a seller')
        q += graph[person]
        searched.add(person)
    return False


search('you')
