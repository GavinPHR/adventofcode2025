with open("4.txt", "r") as f:
    G = [list(line.strip()) for line in f]

D = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
M, N = len(G), len(G[0])
def find(fill=False):
    ans = 0
    for i, row in enumerate(G):
        for j, x in enumerate(row):
            if x != "@":
                continue
            cnt = 0
            for di, dj in D:
                ii, jj = i + di, j + dj
                if 0 <= ii < M and 0 <= jj < N and G[ii][jj] == "@":
                    cnt += 1
            if cnt < 4:
                ans += 1
                if fill:
                    G[i][j] = "."
    return ans
print(find())

ans2 = 0
while True:
    ans = find(fill=True)
    if ans == 0:
        break
    ans2 += ans
print(ans2)
