N,M = map(int,input().split())
graph = []
parent = []*(N+1)
for n in range(N+1):
  parent[n] = n

for m in range(M):
  x,y,z = map(int,input().split())
  graph.append((z,x,y))
graph.sort()
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
def union_parent(parent,a,b):
  a_p = find_parent(parent,a)
  b_p = find_parent(parent,b)
  if a_p > b_p:
    parent[a_p] = b_p
  else:
    parent[b_p] = a_p
total = 0
result = 0
for cost,x,y in graph:
  total += cost
  if find_parent(parent,x) != find_parent(parent,y):
    union_parent(parent,x,y)
    result += cost
print(total-result)