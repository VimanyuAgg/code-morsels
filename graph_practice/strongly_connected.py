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

from collections import OrderedDict

def find_postorders_reverse_graph(postorder,indegree_adj):
    visited = [False]*len(indegree_adj)
    counter = 1

    def dfs(node):
        nonlocal counter
        visited[node] = True
        postorder[node][0] = counter
        counter += 1

        for neighbor in indegree_adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)

        postorder[node][1] = counter
        counter +=1
        return

    for i in range(len(indegree_adj)):
        if not visited[i]:
            dfs(i)

    return

def find_max_postorder_node(postorder):
    '''Returns the index in postordera array which has maximum postorder'''
    max_val = -1
    i = -1
    for index, val in enumerate(postorder):
        if val[1] > max_val:
            max_val = val[1]
            i = index
    return i

def scratch_postorder(entry, postorder):
    for e in entry:
        postorder[e] = [-1,-1]

## Contains implementation using postorder as list of lists, heap, ordered_dict(works!!)
## Not a naive implementation
def number_of_strongly_connected_components(adj):
    indegree_adj = [[] for _ in range(len(adj))]
    # print(indegree_adj)
    for i in range(len(adj)):
        for val in adj[i]:
            indegree_adj[val].append(i)

    # print(indegree_adj)

    # postorder = [[0,0] for _ in range(len(adj))] ## Moving to Ordered Dict to handle large datasets

    postordered_od = OrderedDict({i: [0,0] for i in range(len(adj))})


    # find_postorders_reverse_graph(postorder,indegree_adj)
    find_postorders_reverse_graph(postordered_od,indegree_adj)

    # print(postordered_od)

    # Heap solution not viable as after DFS we need to remove traversed components as well
    # postorder_heap = list((-val[1],node) for node, val in enumerate(postorder))
    # heapq.heapify(postorder_heap)  # adding minus as heapq is min heap
    # print(postorder_heap)

    postordered_od = sorted(postordered_od, key=lambda x: postordered_od[x][1], reverse=True)

    # print(postordered_od)

    visited = [False] * len(adj)
    scc = []

    def do_dfs(node, entry):
        visited[node] = True
        entry.add(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                do_dfs(neighbor, entry)

        return

    while not all(visited):
        # max_postorder_node = find_max_postorder_node(postorder) # Replacing with heap to handle large datasets
        # max_postorder_val, max_postorder_node = heapq.heappop(postorder_heap)
        max_postorder_node = postordered_od[0]
        scc_entry = set()
        do_dfs(max_postorder_node, scc_entry)
        # print(scc_entry)
        scc.append(scc_entry)
        # scratch_postorder(scc_entry, postorder) # Replacing with heap to handle large datasets
        for e in scc_entry:
            postordered_od.remove(e)

    # print(scc)
    return len(scc)

#### NAIVE IMPLEMENTATION BEGINS ####

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
