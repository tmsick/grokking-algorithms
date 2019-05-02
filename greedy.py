from datetime import time

klass_length = {
    'hour': 1,
    'minute': 0,
    'second': 0,
    'microsecond': 0,
}

klasses = {
    'art': {
        'starts_at': time(9, 0)
    },
    'literature': {
        'starts_at': time(9, 30)
    },
    'math': {
        'starts_at': time(10, 0)
    },
    'computer': {
        'starts_at': time(10, 30)
    },
    'music': {
        'starts_at': time(11, 0)
    }
}

for name, data in klasses.items():
    data['ends_at'] = time(
        hour=data['starts_at'].hour + klass_length['hour'],
        minute=data['starts_at'].minute + klass_length['minute'],
        second=data['starts_at'].second + klass_length['minute'],
        microsecond=data['starts_at'].microsecond +
        klass_length['microsecond'])


def get_earliest_klass(klasses, starts_after: time):
    candidates = {
        name
        for name, data in klasses.items() if data['starts_at'] >= starts_after
    }
    if len(candidates) == 0:
        return None
    return min(candidates, key=lambda name: klasses[name]['ends_at'])


starts_after = time(0, 0)
klass = get_earliest_klass(klasses, starts_after)
while klass is not None:
    print(klass)
    klass = get_earliest_klass(klasses, klasses[klass]['ends_at'])
