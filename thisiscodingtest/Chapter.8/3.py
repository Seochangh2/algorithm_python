from collections import defaultdict
N = int(input())

memory = defaultdict(int)
memory[1] = 1
memory[2] = 3

for i in range(3,N+1):
  memory[i] = (memory[i-1] + memory[i-2] * 2) % 796796
  

print(memory[N])