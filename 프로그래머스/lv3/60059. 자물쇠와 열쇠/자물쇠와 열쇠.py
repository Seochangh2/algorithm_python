def rotate_matrix_90(mat):
    n = len(mat)
    m = len(mat[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = mat[i][j]
    return result
def check_lock(lock,N):
    for x in range(N,2*N):
        for y in range(N,2*N):
            if lock[x][y] != 1:
                return False
    return True
def solution(key, lock):
    M = len(key)
    N = len(lock)
    answer = False
    
    new_lock = [[0]*3*N for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            new_lock[(N)+i][(N)+j] = lock[i][j]
    
    for rotate in range(4):
        key = rotate_matrix_90(key)
        for i in range(N*2):
            for j in range(N*2):
                for x in range(M):
                    for y in range(M):
                        new_lock[i+x][j+y] += key[x][y]
                if check_lock(new_lock,N):
                    return True
                for x in range(M):
                    for y in range(M):
                        new_lock[i+x][j+y] -= key[x][y]
    
    
    return answer