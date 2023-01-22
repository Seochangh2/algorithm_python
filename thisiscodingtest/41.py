N,M = map(int,input().split())
graph = []
parent = []
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

for n in range(N+1):
  parent.append(n)
for m in range(M):
  l = list(map(int,input().split()))
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      union_parent(parent,i,j)

vacation =  map(int,input().split())
result = "YES"
for i in range(len(vacation)-1):
  a_p = find_parent(parent,vacation[i])
  b_p = find_parent(parent,vacation[i+1])
  if a_p != b_p:
    result = "NO"
print(result)