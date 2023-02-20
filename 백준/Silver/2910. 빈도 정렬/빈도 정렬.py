import collections

N,C = map(int,input().split())

nums = list(map(int,input().split()))

cnter = collections.Counter(nums)



for n,count in cnter.most_common():
    for c in range(count):
        print(n,end=" ")


