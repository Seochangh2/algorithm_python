N,K = map(int,input().split())
nums = list(map(int,input().split()))
result = sum(nums[0:K])
s = result
for left in range(N-K):
    s = s - nums[left]+nums[left+K]
    result = max(result,s)
print(result)