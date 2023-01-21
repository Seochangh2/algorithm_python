A = list(input())
B = list(input())

def dynamic(s1,s2):
  N = len(s1)
  M = len(s2)
  memory = [ [0]*(M+1) for _ in range(N+1)]
  for i in range(N):
    memory[i+1][0] = i+1
  for i in range(M):
    memory[0][i+1] = i+1

  for n in range(N):
    for m in range(M):
      if s1[n] == s2[m]:
        memory[n+1][m+1] = memory[n][m]
      else:
        memory[n+1][m+1] = 1+min(memory[n][m],memory[n][m+1],memory[n+1][m])
  
  print(memory[N-1][M-1])


dynamic(A,B)