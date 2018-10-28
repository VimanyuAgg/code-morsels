##python2.7

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# [(1, 4), (4, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def recurse(node_map, node, tour, pilot):
    print "**********"
    print "Starting Recurse"
    print "Node_map: {}".format(node_map)
    print "Key Node:{}".format(node)
    print "Current Tour: {}".format(tour)

    if (node_map[node] == []):
        print "node_map[{}] is none".format(node)
        if node == pilot:
            print "node: {} and pilot:{} are equal".format(node, pilot)
            if node_map.values().count([]) == len(node_map.values()):
                print "Base case hit! all the nodes_map vals are None"

                print "all done: final tour: {}".format(tour)
                return tour

            print "Node is pilot but all node_map is not None"
            print "returning None..."
            return None

        print "node is not pilot! returning None..."
        return None

    for val in node_map[node]:
        print "popping val:{} for node_map[{}]".format(val, node)
        node_map[node].remove(val)
        print "popping val:{} for node_map[{}]".format(node, val)
        node_map[val].remove(node)
        print "Node map:{}".format(node_map)
        print "Adding to tour val:{} from node_map[{}]".format(val, node)
        tour.append(val)
        resp = recurse(node_map, val, tour, pilot)
        if resp is None:
            print "tracing back as resp is none"
            print "adding val:{} back to node_map[{}]".format(val, node)
            print "removing val:{} from tour:{}".format(val, tour)
            node_map[node].append(val)
            node_map[val].append(node)
            tour.pop(-1)
            continue
        print "returning tour:{}".format(tour)
        return tour


def find_eulerian_tour(graph):
    # your code here
    node_map = {}
    tour = []
    for i in graph:
        if i[0] not in node_map.keys():
            node_map[i[0]] = []
        node_map[i[0]].append(i[1])

        if i[1] not in node_map.keys():
            node_map[i[1]] = []
        node_map[i[1]].append(i[0])

    pilot = node_map.keys()[0]
    tour.append(pilot)
    print "Node_map:{}".format(node_map)
    print "Node: {} selected as pilot".format(pilot)
    print "Current tour: {}".format(tour)
    print "Calling Recurse"
    return recurse(node_map, pilot, tour, pilot)


# graph=[(1, 2), (2, 3), (3, 1)]
# print find_eulerian_tour(graph)

# graph2 = [(0, 1), (1, 5), (1, 7), (4, 5),
# (4, 8), (1, 6), (3, 7), (5, 9),
# (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
# print find_eulerian_tour(graph2)

graph3 = [(1, 13), (1, 6), (6, 11), (3, 13),
          (8, 13), (0, 6), (8, 9), (5, 9), (2, 6), (6, 10), (7, 9),
          (1, 12), (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9),
          (7, 14), (10, 13)]

graph4 = [(8, 16), (8, 18), (16, 17), (18, 19),
          (3, 17), (13, 17), (5, 13), (3, 4), (0, 18), (3, 14), (11, 14),
          (1, 8), (1, 9), (4, 12), (2, 19), (1, 10), (7, 9), (13, 15),
          (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
