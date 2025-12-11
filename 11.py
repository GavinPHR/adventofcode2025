from collections import defaultdict
G = defaultdict(list)
with open("11.txt", "r") as f:
    for line in f:
        v1, v2s = line.strip().split(":")
        for v2 in v2s.strip().split():
            G[v1].append(v2)

def rec(node, target, memo):
    if node in memo:
        return memo[node]
    if node == target:
        return 1
    if node not in G:
        return 0
    ans = 0
    for v in G[node]:
        ans += rec(v, target, memo)
    memo[node] = ans
    return ans

print(rec("you", "out", {}))
print(rec("svr", "fft", {}) * rec("fft", "dac", {}) * rec("dac", "out", {}))
