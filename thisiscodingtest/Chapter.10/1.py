def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a_p = find_parent(parent,a)
  b_p = find_parent(parent,b)
  if a_p == b_p :
    print("사이클 발생")
    return False
  elif a_p > b_p:
    parent[a_p] = b_p
  else :
    parent[b_p] = a_p
  return True
# 노드와 간선의 개수 입력
V,E = map(int,input().split())

parent = [0]*(V+1)
# 부모를 자기 자신으로 초기화
for v in range(1,V+1):
  parent[v] = v

cycle = False
# union 연산 수행
for e in range(E):
  a,b = map(int,input().split())
  cycle = union_parent(parent,a,b)
  if not cycle:
    break

for v in range(1,V+1):
  print(find_parent(parent,v),end=" ")
print()
for v in range(1,V+1):
  print(parent[v],end=" ")
print()