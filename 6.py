import operator
from functools import reduce

X = []
with open("6.txt", "r") as f:
    for i, line in enumerate(f):
        if line[0] not in ("+", "*"):
            X.append([int(x) for x in line.strip().split()])
        else:
            ops = [(operator.add if x == "+" else operator.mul) for x in line.strip().split()]

ans = 0
for j, op in enumerate(ops):
    if op == operator.add:
        res = 0
    else:
        res = 1
    for i in range(len(X)):
        res = op(res, X[i][j])
    ans += res
print(ans)

M = len(X)
N = len(ops)
X = []
with open("6.txt", "r") as f:
    for line in f:
        if line[0] not in ("+", "*"):
            X.append(line.strip("\n"))
j = 0
k = 0
buffer = []
ans2 = 0
while j < len(X[0]):
    num = 0
    for i in range(M):
        if X[i][j] != " ":
            num = num * 10 + int(X[i][j])
    if num != 0:
        buffer.append(num)
    else:
        ans2 += reduce(ops[k], buffer)
        k += 1
        buffer = []
    j += 1
ans2 += reduce(ops[k], buffer)
print(ans2)
