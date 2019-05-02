stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

states_needed = set()
for states in stations.values():
    states_needed |= states

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for stn, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = stn
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
