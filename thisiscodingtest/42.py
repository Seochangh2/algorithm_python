G = int(input())
P = int(input())
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

graph = [[0]*(P+1) for _ in range(G+1)]
parent = [0]*(G+1)
for g in range(G+1):
  parent[g] = g
result = 0
for p in range(P):
  n = int(input())
  x = find_parent(parent,n)
  if x == 0 :
    break
  result += 1
  union_parent(parent,n,n-1)

print(result)