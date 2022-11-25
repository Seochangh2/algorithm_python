N = int(input())
map = list(input().split())

location = [1,1]
for m in map:
  if m == "L" and location[1] != 1:
    location[1] -= 1
  elif m == "R" and location[1] != N:
    location[1] += 1
  elif m == "U" and location[0] != 1:
    location[0] -= 1
  elif m == "D" and location[0] != N:
    location[0] += 1

print(*location)  