night = input()

location = [int(ord(night[0]) - 96),int(night[1])]

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count = 0
for i,j in steps:
  if (location[0] + i) < 1 or (location[0] + i) > 8:
    continue
  elif (location[1] + j) < 1 or (location[1] + j) > 8:
    continue
  else :
    count += 1

print(count)