from collections import defaultdict
import copy

def all_topological_sorts(adj):
    '''Assumes no '''
    visited = dict()
    indegree= defaultdict(int)

    for node in adj:
        indegree[node] = 0
        visited[node] = False

    for node in adj:
        for neighbor in adj[node]:
            indegree[neighbor] +=1

    print(indegree)
    indegree = dict(indegree)
    res = []
    master_res = []
    topological_sort_helper(adj,visited,indegree,res,master_res)
    print(f"master_res:{master_res}")
    return res

def topological_sort_helper(adj,visited,indegree,res, master_res):
    print("***topological helper starting****")

    if len(res) == len(adj):
        master_res.append(copy.deepcopy(res))

    print(indegree)
    for node in indegree:
        print(visited)
        print(node)
        print(indegree[node])
        print(visited[node])
        if indegree[node] == 0 and (not visited[node]):
            visited[node] = True
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -=1

            topological_sort_helper(adj,visited,indegree,res, master_res)
            print(f"finished node:{node}")

            visited[node] = False
            for neighbor in adj[node]:
                indegree[neighbor] +=1

            res.pop()


adj = {"f":['c','b','a'],
       "c":['d'],
       'b':['d'],
       'd':['e'],
       'a':['e'],
       'e':[],
       'h':['i'],
       'k':['i'],
       'i':[]}

print(all_topological_sorts(adj))