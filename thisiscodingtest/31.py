
    
# import collections,sys
# sys.setrecursionlimit(10**6)
# T = int(input())
# for _ in range(T):
#   N,M = map(int,input().split())

#   nums = list(map(int,input().split()))
#   graph = []
#   # for n in range(N):
#   #   graph.append((nums[(M*n)+0:(M*n)+4]))
#   result = 0
#   memory = collections.defaultdict(int)
#   for n in range(N):
#     memory[n*M] = nums[n*M]
  
#   for m in range(1,M):
#     for n in range(N):
#       up=down=left=0
#       if n == 1:
#         up = 0
#       else :
#         up = memory[(n*M)+m -5]
#       if n == N-1:
#         down = 0
#       else:
#         down = memory[(n*M)+m +3]
#       left = memory[(n*M)+m - 1]

#       memory[(n*M)+m] = max(up,down,left)+nums[(n*M)+m]
  


#   print(memory[N*M-1])
for i in range(7-1,-1,-1):
  print(i)
    

  
N,M = map(int,input().split())
nums = list(map(int,input().split()))
graph = []
result = [[0]*(M) for _ in range(N)]
for n in range(N):
  graph.append((nums[(M*n)+0:(M*n)+4]))
for n in range(N):
  result[n][0] = graph[n][0]
for m in range(1,M):
  for n in range(N):
    if n == 0:
      a = 0
    else:
      a = result[n-1][m-1]
    
    b = result[n][m-1]
    if n == N-1:
      c = 0 
    else:
      c = result[n+1][m-1]
    result[n][m] = graph[n][m]+ max(a,b,c)

print(result)
