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

# 노드와 간선의 개수 입력
V,E = map(int,input().split())
# 간선을 담을 배열, 최종 비용 변수
parent = [0]*(V+1)
edges = []
result = 0
# 부모를 자기 자신으로 초기화
for v in range(1,V+1):
  parent[v] = v


# union 연산 수행
for e in range(E):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

for edge in edges:
  cost,a,b = edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost

print(result)


