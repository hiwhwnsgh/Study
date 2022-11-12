import sys
from typing import *
n,m,r = map(int,sys.stdin.readline().split())
graph = {}
array = [0 for i in range(n)]
for i in range(1,n+1):
    graph[i] = []
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[u].sort(reverse = True)
def dfs(start_v:int)->List[int]:
    results = [0 for i in range(n+1)]
    stack = [start_v]
    count = 1
    while stack:
        v = stack.pop()
        if v not in results:
            results[v] = count
            count+=1
            for i in graph[v]:
                stack.append(i)
    return results


results = dfs(r)
for i in range(1,n+1):
    print(results[i])