points = []
with open("9.txt", "r") as f:
    for line in f:
        i, j = map(int, line.strip().split(","))
        points.append((i, j))
N = len(points)
ans = 0
def area(x1, x2):
    return (abs(x1[0] - x2[0]) + 1) * (abs(x1[1] - x2[1]) + 1)
for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, area(points[i], points[j]))
print(ans)

xs = set()
ys = set()
for x, y in points:
    xs.add(x)
    ys.add(y)
mx = {x: i for i, x in enumerate(sorted(xs))}
my = {y: i for i, y in enumerate(sorted(ys))}
G = [[0] * len(mx) for _ in range(len(my))]
prevy, prevx = my[points[0][1]], mx[points[0][0]]
for x, y in points + [points[0]]:
    if my[y] == prevy:
        for xx in range(min(mx[x], prevx), max(mx[x], prevx) + 1):
            G[my[y]][xx] = 1
    else:
        for yy in range(min(my[y], prevy), max(my[y], prevy) + 1):
            G[yy][mx[x]] = 1
    prevy, prevx = my[y], mx[x]

startx, starty = sorted(points)[0]
q = [(mx[startx] + 1, my[starty] + 1)]
while q:
    x, y = q.pop()
    if G[y][x] > 0:
        continue
    G[y][x] = 2
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(mx) and 0 <= ny < len(my) and G[ny][nx] == 0:
            q.append((nx, ny))

def fully_filled(x1, x2):
    x1 = (mx[x1[0]], my[x1[1]])
    x2 = (mx[x2[0]], my[x2[1]])
    for i in range(min(x1[0], x2[0]), max(x1[0], x2[0]) + 1):
        for j in range(min(x1[1], x2[1]), max(x1[1], x2[1]) + 1):
            if G[j][i] == 0:
                return False
    return True

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        cand = area(points[i], points[j])
        if cand < ans:
            continue
        if fully_filled(points[i], points[j]):
            ans = max(ans, cand)
print(ans)
