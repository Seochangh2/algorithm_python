import math
def solution(dots):
    answer = 0
    dots.sort()
    a = math.pow(dots[0][0]-dots[1][0],2) + math.pow(dots[0][1]-dots[1][1],2)
    b = math.pow(dots[0][0]-dots[2][0],2) + math.pow(dots[0][1]-dots[2][1],2)
    return math.sqrt(a)*math.sqrt(b)