
N = int(input())
food = list(map(int,input().split()))

for f in range(N-2):
  if (food[f]+food[f+2]) >= food[f+1] :
    food[f+2] += food[f]
  else :
    food[f+2] = food[f+1]

print(food[N-1])


# from collections import defaultdict
# N = int(input())
# food = list(map(int,input().split()))
# memory = defaultdict(int)
# memory[0],memory[1] = food[0],food[1]
# for n in range(N-2):
#   memory[n+2] = max(food[n+2]+memory[n],memory[n+1])

# print(memory[N-1])