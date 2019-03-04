# Uses python3

import sys

sys.setrecursionlimit(200000)

# python -m graph_practice.strongly_connected < graph_practice/input_strongly_connected3


# Slightly better Naive Algorithm:
# 1. maintain a list of sets such that for adj{1:[2] , 2:[3],3:[1], 4:[1]}, our list will have [{4},{1,2,3}]
# 2. One vertex can be in atmost one set inside that list because if one vertex is a part of two cycles, we can
# merge those cycles together and call it one cycle.
# 3. create a visited map with statuses UNVISITED, VISITING, VISITED. Initialize with UNVISITED.
# 4. Iterate over vertices in our graph. set state to VISITING.
# run DFS if the status is anything except visited,
# if the source vertex is found in neighbor, we have a cycle -
# return a cycle code, set current node as VISITED, create a set - add current node as well as neighbor to the set.
# return this set back up the stack. Add the set to the list
# Mark all nodes as unvisited
# Choose another vertex from graph and run step 4 again.
# Merge all the sets e.g. [{2,3,4}, {3,5},{1}] -> [{2,3,4,5},{1}]
# Return length of the list


# def number_of_strongly_connected_components(adj):
#     indegree_adj = [[] for _ in range(len(adj))]
#     print(indegree_adj)
#     for i in range(len(adj)):
#         for val in adj[i]:
#             indegree_adj[val].append(i)
#
#     print(indegree_adj)


def merge_sets(list_of_sets):
    new_list = []
    taken = [False]*len(list_of_sets)

    def dfs(index, setz):
        taken[index] = True
        new_set = setz
        for j, other_setz in enumerate(list_of_sets):
            if not taken[j] and not (new_set.isdisjoint(other_setz)):
                new_set.update(dfs(j, other_setz))

        return new_set

    for i, sez in enumerate(list_of_sets):
        if not taken[i]:
            new_list.append(dfs(i,sez))

    return new_list




def number_of_strongly_connected_components_naive(adj):
    '''works'''

    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    cycles = [] # list of sets

    def _get_relevant_sets(node):
        nonlocal cycles
        cycles = merge_sets(cycles)
        for c in cycles:
            if node in c:
                return c

        return set()

    def dfs(node,source):
        rel_set = _get_relevant_sets(node)
        # print(f"rel_set for node:{node}, source:{source} is {rel_set}")
        visited[node] = VISITING

        # print(f"adj[{node}]: {adj[node]}")
        for neighbor in adj[node]:

            if visited[neighbor] == VISITING and neighbor == source:
                # Found a cycle which ends at source
                rel_set.add(node)
                rel_set.add(neighbor)
                cycles.append(rel_set)
                return "Found", rel_set

            if visited[neighbor] == VISITING:
                pass

            elif visited[neighbor] != VISITED:
                res_code, res_set = dfs(neighbor, source)

                if res_code == "Found":
                    res_set.add(node)
                    cycles.append(res_set)
                    visited[node] = VISITED
                    return "Found", res_set

        visited[node] = VISITED
        rel_set.add(node)
        cycles.append(rel_set)

        return "", rel_set

    for i in range(len(adj)):
        visited = dict({i: UNVISITED for i in range(len(adj))})
        dfs(i,i)

    # print(f"cycles: {cycles}")
    cycles = merge_sets(cycles)
    # print(f"cycles: {cycles}")
    return len(cycles)


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
