def my_hash(s):
    return ord(s[0].lower()) - ord('a')


def set_item(key, val, table):
    realm = table[my_hash(key)]
    for i in range(len(realm)):
        if realm[i][0] == key:
            realm[i] = (key, val)
            return
    realm.append((key, val))


def get_item(key, table):
    realm = table[my_hash(key)]
    for k, v in realm:
        if k == key:
            return v
    return None


table = [[] for i in range(26)]
items = ['apple', 'banana', 'avocado']
for i, item in enumerate(items):
    set_item(item, i, table)
for item in items:
    print(get_item(item, table))
