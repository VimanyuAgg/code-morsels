#Uses python3

import sys
# import queue

from collections import deque

def distance(adj, s, t):
    '''Finds shortest distance between s & t'''
    # print(adj)

    # adj = list(map(list,map(set, adj)))

    adj = list(map(set,adj))

    # print(adj)
    if adj is None or len(adj) == 0:
        return -1

    # q = queue.Queue()
    # q.put(s)
    q = deque()
    q.append(s)
    dist = [sys.maxsize]*len(adj)
    dist[s] = 0

    while len(q):
        node = q.popleft()

        for neighbor in adj[node]:

            if dist[neighbor] == sys.maxsize:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

            if neighbor == t:
                return dist[neighbor]

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
