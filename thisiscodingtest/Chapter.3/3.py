N,M = map(int,input().split())

cards = []
mins = []
for n in range(N):
  cards.append(min(list(map(int,input().split()))))

print(max(cards))


