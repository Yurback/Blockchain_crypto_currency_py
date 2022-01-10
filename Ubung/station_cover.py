states_needed = set(['mt', 'or', 'wa', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}

stations["kone"] = {'id','nv','ut'}
stations["ktwo"] = {'wa','id','mt'}
stations["kthree"] = {'or','nv','ca'}
stations["kfour"] = {'nv','ut'}
stations["kfive"] = {'ca','az'}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
    # key          value
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered

print(final_stations)

