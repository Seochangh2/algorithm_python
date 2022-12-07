import collections
# 노드와 간선의 개수 입력
V,E = map(int,input().split())
# 간선을 담을 배열
indegree = [0]*(V+1)
graph = collections.defaultdict(list)

for e in range(E):
  a,b = map(int,input().split())
  graph[a].append(b)
  indegree[b] += 1


def topology_sort():
  result = []
  q = collections.deque()
  for i in range(1,V+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    node = q.popleft()
    result.append(node)

    for g in graph[node]:
      indegree[g] -= 1
      if indegree[g] == 0:
        q.append(g)

  print(*result)

topology_sort()  