from collections import defaultdict
from sys import maxsize
N , M = map(int,input().split())
money = []
for n in range(N):
  money.append(int(input()))

money.sort()
memo = defaultdict(int)
def dynamic(num):
  if num == 0 :
    return 0
  if num < money[0]:
    return -1


  if num in memo:
    return memo[num] 
  min_result = maxsize
  for m in money:
    if num >= m :
      check = dynamic(num-m)
      if check != -1:
        min_result = min(min_result,check)
  if min_result == maxsize:
    return -1

  memo[num] = min_result+1
  return memo[num] 

result = dynamic(M)
print(result)