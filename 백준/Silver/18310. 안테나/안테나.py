N = int(input())
home = list(map(int,input().split()))
home.sort()


print(home[(len(home)-1)//2])