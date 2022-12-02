from collections import defaultdict

memory = defaultdict(int)
memory[1] = 0
num = int(input())

for n in range(2,num+1):
  memory[n] = memory[n-1]+1
  if n % 5 == 0 :
    memory[n] = min(memory[n],memory[n//5]+1)
  if n % 3 == 0:
    memory[n] = min(memory[n],memory[n//3]+1)
  if n % 2 == 0 :
    memory[n] = min(memory[n],memory[n//2]+1)

print(memory[num])