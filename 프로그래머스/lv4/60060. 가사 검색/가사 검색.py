import bisect,collections
def solution(words, queries):
    answer = []
    memory = collections.defaultdict(list)
    r_memory = collections.defaultdict(list)
    for w in words:
        memory[len(w)].append(w)
        r_memory[len(w)].append(w[::-1])

    for v in memory:
        memory[v].sort()
        r_memory[v].sort()
        

    def bisect_sol(m,l,r):
        left = bisect.bisect_left(m,l)
        right = bisect.bisect_right(m,r)
        return right-left
    for q in queries:
        if "?" == q[-1]:
            answer.append(bisect_sol(memory[len(q)],q.replace('?','a'),q.replace('?','z')))
        elif "?" == q[0]:
            answer.append(bisect_sol(r_memory[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z')))

        
    return answer