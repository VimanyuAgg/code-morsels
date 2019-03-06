#Uses python3

import sys


def negative_cycle(adj, cost):
    # Find if negative weight cycle exists in the graph
    # return 1 if it exists else return 0
    # Bellman Ford

    dist = [sys.maxsize]*len(adj)

    dist[0] = 0

    for _ in range(len(adj)-1):
        relax_all_edges(adj,cost,dist)

    if relax_all_edges(adj,cost,dist):
        return 1

    return 0


def relax_all_edges(adj,cost,dist):

    changed = False

    for node in range(len(adj)):
        for index, neighbor in enumerate(adj[node]):
            if dist[neighbor] > dist[node] + cost[node][index]:
                changed = True
                dist[neighbor] = dist[node] + cost[node][index]

    return changed


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
