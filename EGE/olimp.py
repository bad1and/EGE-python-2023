def cp(N, M, K):
    matrix = [[0] * M for _ in range(N)]

    counter = 0
    for i in range(N):
        for j in range(M):
            if 0 < j < len("0" * M) - 1:
                matrix[i][j] = i * M + j + 1
                diff1 = abs(matrix[i][j] - matrix[i][j - 1])
                diff2 = abs(matrix[i][j] - matrix[i][j + 1])
                diff3 = abs(matrix[i][j] - matrix[i][j])

                diff4 = abs(matrix[i + 1][j] - matrix[i + 1][j - 1])
                diff5 = abs(matrix[i + 1][j] - matrix[i + 1][j + 1])
                diff6 = abs(matrix[i + 1][j] - matrix[i + 2][j])

                diff7 = abs(matrix[i + 2][j] - matrix[i + 2][j - 1])
                diff8 = abs(matrix[i + 2][j] - matrix[i + 2][j + 1])
                diff9 = abs(matrix[i + 2][j] - matrix[i + 3][j])

                diff11 = abs(matrix[i + 3][j] - matrix[i + 3][j + 1])

                if (diff1 < K and diff2 < K and diff3 < K):
                    counter += 1

    return counter


# [0 ,0 ,0 ,0]
# [0 ,0 ,0 ,0]
# [0 ,0 ,0 ,0]
# [0 ,0 ,0 ,0]

N = int(input())
M = int(input())
K = int(input())

result = cp(N, M, K)
# print(result)

import http.client
def pc(n,m,k):
    matrix = [[0] * m for _ in range(n)]
    counter = 0
    for i in range(n):
        for j in range(m):
            matrix[i][j] = i * m + j + 1
            if j > 0:
                diff = abs(matrix[i][j] - matrix[i][j - 1])
                if diff < k:
                    counter += 1

    return counter


n = int(input())
m = int(input())
k = int(input())

result = pc(n, m, k)
print(result)
