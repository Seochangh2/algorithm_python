from itertools import combinations

N = int(input())
nums = list(map(int,input().split()))

nums.sort()

target = 1

for n in nums:
  if target<n:
    break
  target += n

print(target)