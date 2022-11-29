N,K = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)
for k in range(K):
  A[k] = B[k]

print(sum(A))