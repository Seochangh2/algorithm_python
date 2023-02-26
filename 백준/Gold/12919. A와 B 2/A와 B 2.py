S = list(input())
T = list(input())

s_len = len(S)
t_len = len(T)
result = 0
def back(s,t):
    global result
    if len(s) == len(t) and s == t:
        result = 1
        return
    elif len(s) < len(t):
        if t[0] == 'B':
            t.reverse()
            t.pop()            
            back(s,t)
            t.append("B")
            t.reverse()
        if t[-1] == 'A':
            t.pop()
            back(s,t)
            t.append("A")
            
    
back(S,T)
print(result)