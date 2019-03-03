#Uses python3

import sys


def acyclic(adj):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    state = dict({i: UNVISITED for i in range(len(adj))})
    # print(adj)
    def _explore(node):
        # print(f"exploring node:{node}")
        state[node] = VISITING
        for neighbor in adj[node]:
            # print(f"visiting neighbour:{neighbor} for node:{node}")
            if state[neighbor] == VISITING:
                # print(f"node:{node} returning 1")
                return 1  # cycle exists

            elif state[neighbor] == VISITED:
                continue
            else:
                # unvisited neighbour
                if _explore(neighbor) == 1:
                    return 1

        state[node] = VISITED
        # print(f"node:{node} returning 0")
        return 0

    for i in range(len(adj)):
        if state[i] != VISITED:
            # print(f"****New Exploration: node:{i}*****")
            res = _explore(i)
            # print(f"Node:{i} exploration yielded: {res}")
            if res == 1:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
