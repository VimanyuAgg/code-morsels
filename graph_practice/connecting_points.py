#Uses python3
import sys
import math
import heapq


def minimum_distance(x, y):
    ## Uses Prim's algorithm
    result = 0

    # for i in range(len(x)):
    #     print(x[i],y[i])

    cost = [sys.maxsize]*len(x)

    cost[0] = 0
    heap = []
    c_dict = dict() #  cost dictionary to maintain lookup - help in change priority phase

    for i in range(len(x)):
        heap.append((cost[i], i))
        c_dict[i] = cost[i]

    heapq.heapify(heap)

    while len(c_dict):
        dist, node = heapq.heappop(heap)
        # print(f"node popped: {node}")
        # print(f"c_dict:{c_dict}")

        if node not in c_dict or c_dict[node] != dist:
            continue

        c_dict.pop(node)

        for i in range(len(x)):
            if i == node or (i not in c_dict):
                continue

            dist_i = compute_cartisian_dist(i, x, y,node)
            if cost[i] > dist_i:
                cost[i] = dist_i
                c_dict[i] = cost[i]
                heapq.heappush(heap, (cost[i], i))

    # print(cost)
    result = sum(cost)
    return result


def compute_cartisian_dist(i, x, y,node):
    x1 = x[node] - x[i]
    y1 = y[node] - y[i]

    return math.sqrt(x1**2 + y1**2)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
