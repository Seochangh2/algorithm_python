import sys
input = sys.stdin.readline
N = int(input())
players = list(map(int,input().rstrip().split()))
players.sort()

result = counter = 0

for p in players:
  counter += 1
  if counter>=p:
    result += 1
    counter = 0

print(result)