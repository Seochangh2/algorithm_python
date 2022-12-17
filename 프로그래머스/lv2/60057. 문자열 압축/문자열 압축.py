import sys
def solution(s):
    answer = 0
    leng = len(s)
    if leng == 1:
        return 1
    min_result = sys.maxsize
    for s_l in range(1,(leng//2)+1):

        count = []
        now = s_l
        pre = s[:s_l]
        cnt = 1
        while now+s_l <= leng:
            now_s = s[now:now+s_l]
            if pre == now_s:
                pre = now_s
                cnt += 1
            else :
                if cnt>=2:
                    count.append(str(cnt))
                count.append(pre)
                pre = now_s
                cnt = 1
            now+=s_l
            if now+s_l > leng:
                if cnt>=2:
                    count.append(str(cnt))
                count.append(pre)
                pre = now_s
                cnt = 1
                count.append(s[now:])
        result = ''.join(count)
        if len(result) < min_result:
            min_result = len(result)
            
    return min_result