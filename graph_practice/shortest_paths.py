#Uses python3

import sys
from collections import deque


def relax_all_edges(adj, cost, distance,last_iter = False):

    if not last_iter:
        for node in range(len(adj)):
            if distance[node] != 10**19:
                #  We do not want to iterate over nodes which cannot be reached by source
                for index, neighbor in enumerate(adj[node]):
                    if distance[neighbor] > cost[node][index] + distance[node]:
                        distance[neighbor] = cost[node][index] + distance[node]

        return

    else:
        neg_cycle_edges = set()
        for node in range(len(adj)):
            if distance[node] != 10 ** 19:
                for index, neighbor in enumerate(adj[node]):
                    if distance[neighbor] > cost[node][index] + distance[node]:
                        neg_cycle_edges.add(node)
                        distance[neighbor] = cost[node][index] + distance[node]

        return neg_cycle_edges


def find_all_edges_reachable_by_neg_cycle(adj,neg_weight_nodes_set):
    q = deque()

    for n in neg_weight_nodes_set:
        q.append(n)

    visited = [False]*len(adj)

    while len(q):
        node = q.popleft()
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor] and neighbor not in neg_weight_nodes_set:
                neg_weight_nodes_set.add(neighbor)
                q.append(neighbor)

    return neg_weight_nodes_set


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    '''Solution for infinite arbitrage'''
    distance[s] = 0
    reachable[s] = 1  # 1 means reachable, 0 means non-reachable
    shortest[s] = 1   # 1 means shortest exists, 0 means shortest doesn't exist

    for _ in range(len(adj)-1):
        relax_all_edges(adj,cost,distance)

    neg_weight_nodes_set = relax_all_edges(adj,cost,distance, last_iter=True)

    if len(neg_weight_nodes_set):
        neg_weight_nodes_set = find_all_edges_reachable_by_neg_cycle(adj, neg_weight_nodes_set)

    for n in neg_weight_nodes_set:
        shortest[n] = 0

    for n in range(len(distance)):
        if distance[n] != 10**19:
            reachable[n] = 1

    return


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

