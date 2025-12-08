from collections import Counter
class Point:
    def __init__(self, x, y, z, i):
        self.x = x
        self.y = y
        self.z = z
        self.i = i

    def sqdist(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

points = []
with open("8.txt", "r") as f:
    for i, line in enumerate(f):
        x, y, z = map(int, line.strip().split(","))
        points.append(Point(x, y, z, i))
N = len(points)
dist_pairs = []
for i in range(N):
    for j in range(i + 1, N):
        d = points[i].sqdist(points[j])
        dist_pairs.append((d, i, j))
dist_pairs.sort()

uf = list(range(N))
def find(u):
    if uf[u] != u:
        uf[u] = find(uf[u])
    return uf[u]

for idx in range(1000):
    _, i, j = dist_pairs[idx]
    ri, rj = find(i), find(j)
    uf[ri] = rj
for i in range(N):
    find(i)
ans = 1
for parent, size in Counter(uf).most_common(3):
    ans *= size
print(ans)

visited = set()
for _, i, j in dist_pairs:
    visited.add(i)
    visited.add(j)
    if len(visited) == N:
        print(points[i].x * points[j].x)
        break

