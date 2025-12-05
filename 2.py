import math

intervals = []
with open("2.txt", "r") as f:
    for lr in f.read().strip().split(","):
        l, r = lr.split("-")
        intervals.append((int(l), int(r)))

def split_intervals(l, r, notest=False):
    res = []
    lo = l
    r_cnt = len(str(r))
    lo_cnt = len(str(lo))
    while lo_cnt < r_cnt:
        if notest or lo_cnt % 2 == 0:
            res.append((lo, 10 ** lo_cnt - 1))
        lo = 10 ** lo_cnt
        lo_cnt += 1
    if notest or r_cnt % 2 == 0:
        res.append((lo, r))
    return res

clean_intervals = []
for l, r in intervals:
    clean_intervals.extend(split_intervals(l, r))

def count(l, r, parts=2):
    ans = set()
    k = len(str(l)) // parts
    lo = int(str(l)[:k])
    hi = int(str(r)[:k])
    for i in range(lo, hi + 1):
        cand = 0
        for j in range(parts - 1, -1, -1):
            cand += i * 10 ** (k * j)
        if l <= cand <= r:
            ans.add(cand)
    return ans


ans = set()
for l, r in clean_intervals:
    ans |= count(l, r)
print(sum(ans))

clean_intervals = []
for l, r in intervals:
    clean_intervals.extend(split_intervals(l, r, notest=True))
ans2 = set()
for l, r in clean_intervals:
    length = len(str(l))
    for parts in range(2, length + 1):
        if length % parts == 0:
            ans2 |= count(l, r, parts)
print(sum(ans2))
