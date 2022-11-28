import sys
import collections
N,M = map(int,sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
start_v = []
count = 0
for i in range(1,N+1):
    if graph[i]:
        stack = [i]
        count = 1
        break

while True:
    if N == len(start_v):
        break
    if not stack:
        for i in range(1,N+1):
            if i not in start_v:
                stack.append(i)
                count+=1
                break
    node = stack.pop()
    if node not in start_v:
        start_v.append(node)
        for i in graph[node]:
            stack.append(i)
print(count)