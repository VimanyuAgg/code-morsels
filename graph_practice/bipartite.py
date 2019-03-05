#Uses python3

import sys
import queue

from collections import deque

def bipartite(adj):

    adj = list(map(set,adj))

    color = [-1]*len(adj)

    if adj is None or len(adj) == 0:
        return 1

    q = deque()

    q.append(0)
    counter = 0
    color[0] = counter % 2

    while len(q):

        node = q.popleft()
        counter = color[node] + 1

        for neighbor in adj[node]:

            if color[neighbor] == -1:
                color[neighbor] = counter % 2
                q.append(neighbor)

            elif node != neighbor and color[neighbor] == color[node]:
                return 0

    return 1

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
    print(bipartite(adj))
