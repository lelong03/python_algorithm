def distance(network):

    network_map = {}
    root = None

    for idx, value in enumerate(network):
        if idx not in network_map:
            network_map[idx] = []
        if value not in network_map:
            network_map[value] = []
        if value == idx:
            root = value
            continue
        network_map[idx].append(value)
        network_map[value].append(idx)

    distance_map = [0] * (len(network) - 1)
    passed = set({root})
    neighbors = [[root], []]
    counter = 0
    set_idx = 0
    while neighbors[set_idx]:
        next_set_idx = (set_idx + 1) % 2
        if counter > 0:
            distance_map[counter - 1] += len(neighbors[set_idx])
        for neighbor in neighbors[set_idx]:
            for next_neighbor in network_map[neighbor]:
                if next_neighbor in passed:
                    continue
                passed.add(next_neighbor)
                neighbors[next_set_idx].append(next_neighbor)
        neighbors[set_idx] = []
        set_idx = next_set_idx
        counter += 1
    return distance_map


T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
print(distance(T))
