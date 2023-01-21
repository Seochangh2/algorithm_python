import collections
N = int(input())
ugly = collections.defaultdict(int)
ugly[0] = 1
i2=i3=i5=0

next2,next3,next5 = 2,3,5

for idx in range(1,N):
  ugly[idx] = min(next2,next3,next5)

  if ugly[idx] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[idx] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[idx] == next5:
    i5 += 1
    next5 = ugly[i5] * 5


print(ugly[N-1])
        