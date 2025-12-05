intervals = []
xs = []
mode = True
with open("5.txt", "r") as f:
    for line in f:
        if line == "\n":
            mode = False
            continue
        if mode:
            l, r = line.strip().split("-")
            intervals.append((int(l), int(r)))
        else:
            xs.append(int(line.strip()))
xs.sort()
intervals.sort()
merged = []
lo, hi = intervals[0]
for l, r in intervals:
    if l <= hi:
        hi = max(hi, r)
    else:
        merged.append((lo, hi))
        lo, hi = l, r
merged.append((lo, hi))
ans = 0
i = 0
for x in xs:
    while i < len(merged) and merged[i][1] < x:
        i += 1
    if i < len(merged) and merged[i][0] <= x <= merged[i][1]:
        ans += 1
print(ans)

print(sum(r - l + 1 for l, r in merged))