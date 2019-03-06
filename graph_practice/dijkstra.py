#Uses python3

import sys
import heapq

def distance(adj, cost, s, t):
    # print(adj)
    # print(cost)
    heap = []
    distance_from_s = dict()

    for i in range(len(adj)):
        heap.append((sys.maxsize,i))
        distance_from_s[i] = sys.maxsize

    distance_from_s[s] = 0

    heap.append((0, s))
    heapq.heapify(heap)
    # print(distance_from_s)
    # print("*****")
    while len(distance_from_s):

        d, node = heapq.heappop(heap)
        # print(f"node: {node}, d:{d}")

        if node not in distance_from_s or distance_from_s[node] != d:
            continue

        if node == t and d != sys.maxsize:
            return d

        distance_from_s.pop(node)

        for i, neighbor in enumerate(adj[node]):

            # print(f"node: {node}, neighbor:{neighbor}, index:{i}")

            if neighbor in distance_from_s and distance_from_s[neighbor] > cost[node][i] + d:
                distance_from_s[neighbor] = cost[node][i] + d
                heapq.heappush(heap, (distance_from_s[neighbor], neighbor))

            # print(distance_from_s)


    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
