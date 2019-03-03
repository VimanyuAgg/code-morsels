#Uses python3

import sys

sys.setrecursionlimit(200000)

# python -m graph_practice.strongly_connected < graph_practice/input_strongly_connected3


def number_of_strongly_connected_components(adj):
    result = 0
    cycles = set()

    def can_round_about(node, source):
        # print(f"can_round_about called for: node,source: {node, source}")

        for neighbor in adj[node]:
            if neighbor == source:
                # Found a cycle!
                # print(f"original source:{source} is a neighbor of node:{node}")
                cycles.add(node)
                return True

            else:
                if can_round_about(neighbor, source):
                    cycles.add(node)
                    return True

        # print(f"returning False for node:{node}, source: {source}")
        return False

    for i in range(len(adj)):
            # print(f"Starting new round about for {i}")
            if i in cycles:
                continue
            if can_round_about(i, i):
                cycles.add(i)
            result += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
