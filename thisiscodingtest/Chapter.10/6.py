import collections

N = int(input())

graph = [[] for i in range(N+1)]
indegree = [0] * (N+1) 
time =[0]*(N+1)

for n in range(1,N+1):
  inp = list(map(int,input().split()))
  time[n] = inp[0]
  for i in range(1,len(inp)):
    if inp[i] == -1:
      break
    indegree[n] += 1
    graph[inp[i]].append(n)

def topology_sort():
  result = [0]*(N+1)
  q = collections.deque()
  for i in range(1,N+1):
    if indegree[i] == 0:
      q.append(i)
      result[i] = time[i]

  while q:
    node = q.popleft()

    for g in graph[node]:
      indegree[g] -= 1
      if indegree[g] == 0: 
        q.append(g)
        result[g] = result[node] + time[g]
  
  for i in range(1,N+1):
    print(result[i])

topology_sort()