from copy import deepcopy

with open("3.txt", "r") as f:
    X = [[int(i) for i in line.strip()] for line in f]
M, N = len(X), len(X[0])
Y = deepcopy(X)
for i in range(M):
    for j in range(N - 2, -1, -1):
        Y[i][j] = max(Y[i][j], Y[i][j + 1])

ans = 0
for i in range(M):
    local_max = 0
    for j in range(N - 1):
        local_max = max(local_max, X[i][j] * 10 + Y[i][j + 1])
    ans += local_max
print(ans)

def best_idx(arr, i, j):
    if i == j:
        return i
    ret = i
    best_val = arr[i]
    for k in range(i + 1, j + 1):
        if arr[k] > best_val:
            best_val = arr[k]
            ret = k
    return ret

ans2 = 0
for i in range(M):
    local_max = 0
    start = 0
    for j in range(12, 0, -1):
        idx = best_idx(X[i], start, N - j)
        local_max = local_max * 10 + X[i][idx]
        start = idx + 1
    ans2 += local_max
print(ans2)
