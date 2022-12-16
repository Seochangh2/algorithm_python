import itertools

N,M = map(int,input().split())

nums = list(map(int,input().split()))

cnt = 0

for (a,b) in itertools.combinations(nums,2):
  if a!=b:
    cnt +=1

print(cnt)
