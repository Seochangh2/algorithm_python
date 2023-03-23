import bisect,sys
input = sys.stdin.readline
N,M = map(int,input().split())
titles = []
titles_p = []
powers = []
for n in range(N):
    t,n = input().split()
    titles.append(t)
    titles_p.append(int(n))
for m in range(M):
    p = int(input())
    i = bisect.bisect_left(titles_p,p)
    print(titles[i])
