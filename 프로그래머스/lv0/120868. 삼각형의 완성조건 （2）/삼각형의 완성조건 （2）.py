def solution(sides):
    answer = 0
    sides.sort()
    a = sum(sides) - sides[1] - 1
    b= sum(sides) - sides[1] 
    return a+b