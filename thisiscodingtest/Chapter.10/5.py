def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a_p = find_parent(parent,a)
  b_p = find_parent(parent,b)
  if a_p > b_p:
    parent[a_p] = b_p
  else :
    parent[b_p] = a_p

N,M = map(int,input().split())
# 간선을 담을 배열, 최종 비용 변수
parent = [0]*(N+1)
edges = []
result = []
# 부모를 자기 자신으로 초기화
for n in range(1,N+1):
  parent[n] =n

for m in range(M):
  a,b,c = map(int,input().split())
  edges.append((c,a,b))
edges.sort()

for edge in edges:
  cost,a,b = edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result.append(cost)

print(sum(result)-max(result))

