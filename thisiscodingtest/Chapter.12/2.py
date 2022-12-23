import heapq
S = input()
s_li= []
n = 0
for s in S:
  if s.isdigit():
    n += int(s)
  else:
    s_li.append(s)
s_li.sort()
for s in s_li:
  print(s,end="")
print(n)