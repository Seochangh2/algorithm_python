import sys,collections
sys.setrecursionlimit(10**7)
N,target = map(int,input().split())


def sol(num):
    q = collections.deque([num])
    visited=[[-1,0] for _ in range(100001)]
    visited[num][0] = 0
    visited[num][1] = 1
    while q:
        x = q.popleft()
        for i in [x-1,x+1,x*2]:
            if 0<=i<=100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] += visited[x][1]
                    q.append(i)
                elif visited[i][0] == visited[x][0]+1:
                    visited[i][1] += visited[x][1]
    print(visited[target][0])
    print(visited[target][1])
sol(N)
