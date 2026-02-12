def brute(matrix):
    n=len(matrix)
    rotated=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1]=matrix[i][j]
    return rotated
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(brute(matrix))

def optimal(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(optimal(matrix))