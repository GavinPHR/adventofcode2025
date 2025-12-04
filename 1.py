cur = 50
cnt = 0
with open("1.txt", "r") as f:
    for line in f:
        cur += (1 if line[0] == "R" else -1) * int(line[1:])
        cnt += (cur % 100) == 0
print(cnt)

cur = 50
ldiv = 0
lmod = 50
cnt = 0
with open("1.txt", "r") as f:
    for line in f:
        cur += (1 if line[0] == "R" else -1) * int(line[1:])
        rdiv, rmod = divmod(cur, 100)
        if rdiv > ldiv:
            cnt += rdiv - ldiv
        elif rdiv == ldiv:
            cnt += rmod == 0
        else:
            cnt += ldiv - rdiv - (lmod == 0) + (rmod == 0)
        ldiv, lmod = rdiv, rmod
print(cnt)
