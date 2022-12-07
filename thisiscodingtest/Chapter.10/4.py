N , M = map(int,input().split())

result = []

parent = []
for n in range(N+1):
  parent.append(n)
def find_team(parent,x):
  if parent[x]!= x:
    parent[x]= find_team(parent,parent[x])
  return parent[x]

def union_team(parent,a,b):
  a_t = find_team(parent,a)
  b_t = find_team(parent,b)
  if a_t < b_t:
    parent[b_t] = a_t
  else :
    parent[a_t] = b_t

for m in range(M):
  op,a,b = map(int,input().split())
  if op == 0 :
    union_team(parent,a,b)
  else :
    a_t = find_team(parent,a)
    b_t = find_team(parent,b)
    if a_t != b_t:
      result.append("NO")
    else:
      result.append("YES")

for r in result:
  print(r)