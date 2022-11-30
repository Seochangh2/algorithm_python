import sys
N = int(input())
have = list(map(int,(sys.stdin.readline().rstrip()).split()))
M = int(input())
request = list(map(int,(sys.stdin.readline().rstrip()).split()))
have.sort()

def binary_search(target,nums,start,end):

  while start <= end:
    mid = (start+end)//2
    if nums[mid] == target:
      return 1
    elif nums[mid] > target:
      end = mid-1
    else :
      start = mid+1

  return -1
result = []
for r in request:
  if binary_search(r,have,0,N-1) == 1:
    result.append("yes")
  elif binary_search(r,have,0,N-1) == -1:
    result.append("no")

print(*result)