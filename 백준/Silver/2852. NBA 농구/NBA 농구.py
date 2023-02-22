N = int(input())
goals = []
result=[0 for _ in range(3)]
score = [0 for _ in range(3)]
for n in range(N):
    goals.append(list(input().split()))
def string_to_int(time):
    h = int(time[0:2]) 
    m = int(time[3:5])
    return h*60 + m
def int_to_string(time):
    h = str(time//60)
    m = str(time % 60)
    if len(h) == 1 :
        h = "0"+h
    if len(m) == 1 :
        m = "0"+m
    
    return h+":"+m

pre = string_to_int(goals[0][1])
score[int(goals[0][0])] += 1

for i in range(1,N):
    s_team,s_time = goals[i][0],goals[i][1]
    time = string_to_int(s_time)
    team = int(s_team)

    if score[1] > score[2]:
        win_team = 1
    elif score[2] > score[1]:
        win_team = 2
    else:
        pre = time   
    result[win_team] += time - pre
    pre = time
    score[team] += 1        

if score[1] > score[2]:
    win_team = 1
    result[win_team] += (48*60) - pre
elif score[2] > score[1]:
    win_team = 2
    result[win_team] +=  (48*60) - pre
else:
    pre = time   
for i in range(1,3):
    print(int_to_string(result[i]))