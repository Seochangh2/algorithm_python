N = int(input())

switch = [0]+list(map(int,input().split()))
st_n = int(input())
students = []

for n in range(st_n):
    students.append(list(map(int,input().split())))
    
for sex,num in students:
    if sex == 1:
        i = 1
        while (num*i) <= N:
            if switch[num*i] == 0:
                switch[num*i] = 1
            else :
                switch[num*i] = 0
            i += 1

    elif sex == 2:
        left,right = num-1,num+1
        while True :
            if left < 1 or right > N:
                left += 1
                right -= 1
                break
            elif switch[left] != switch[right]:
                left += 1
                right -= 1
                break
            elif switch[left] == switch[right]:
                left -= 1
                right += 1

        if left != right:
            for i in range(left,right+1):
                if switch[i] == 0:
                    switch[i] = 1
                else :
                    switch[i] = 0
        else:
            if switch[num] == 0:
                switch[num] = 1
            else :
                switch[num] = 0
suf = N//20
switch.pop(0)
if suf == 0:
    print(*switch)
else :
    for i in range(suf):
        print(*switch[ 20*i : 20*i+20 ])
    print(*switch[20*suf:])

