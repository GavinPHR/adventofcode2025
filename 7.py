with open("7.txt", "r") as f:
    G = [[x for x in line.strip()] for line in f]

N, M = len(G), len(G[0])
b = [0] * M
b[G[0].index("S")] = 1
ans = 0
for i in range(1, N):
    b_ = [0] * M
    for j in range(M):
        if b[j]:
            if G[i][j] == "^":
                ans += 1
                b_[j - 1] += b[j]
                b_[j + 1] += b[j]
            else:
                b_[j] += b[j]
    b = b_
print(ans)
print(sum(b))
