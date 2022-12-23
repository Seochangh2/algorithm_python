import itertools
def solution(n, weak, dist):
    answer = len(dist)+1
    length = len(weak)
    for i in range(length):
         weak.append(weak[i]+n)
    dist_per = list(itertools.permutations(dist,len(dist)))
    
    for start in range(length):
        
        for friends in dist_per:
            cnt = 1
            area = weak[start] + friends[cnt-1]
            for idx in range(start,start+length):
                if weak[idx] > area:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    area = weak[idx]+friends[cnt-1]
            answer = min(answer,cnt)
    if answer>len(dist):
        return -1
        
    return answer