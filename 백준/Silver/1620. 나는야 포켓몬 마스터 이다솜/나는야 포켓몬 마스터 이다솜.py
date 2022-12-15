import collections
import sys
N , M = map(int,input().split())
input = sys.stdin.readline
pok = {}

for i in range(1,N+1):
    p =input().rstrip()
    pok[i] = p
    pok[p] = i
    
for m in range(M):
    quest = input().rstrip()
    if quest.isdigit() :
        print(pok[int(quest)])
    else:
        print(pok[quest])