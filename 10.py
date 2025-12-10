import numpy as np
from scipy.optimize import linprog
from collections import deque

class Line:
    def __init__(self, line):
        parts = line.strip().split()
        target_str = parts[0][1:-1]
        self.n = len(target_str)
        self.p = len(parts) - 2
        self.target = 0
        for i, c in enumerate(target_str):
            self.target |= 1 << i if c == "#" else 0
        self.buttons = []
        self.A = np.zeros((self.n, self.p), dtype=int)
        self.b = np.array([int(x) for x in parts[-1][1:-1].split(",")], dtype=int)
        for i, part in enumerate(parts[1:-1]):
            button = 0
            for c in part[1:-1].split(","):
                button |= 1 << int(c)
                self.A[int(c), i] = 1
            self.buttons.append(button)

    def solve(self):
        q = deque([(0, 0)])
        visited = set()
        while q:
            state, presses = q.popleft()
            for button in self.buttons:
                new_state = state ^ button
                if new_state == self.target:
                    return presses + 1
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, presses + 1))
        return -1

    def solve_lp(self):
        c = np.ones(self.p)
        return int(linprog(c, A_eq=self.A, b_eq=self.b, integrality=1).fun)

    def __repr__(self):
        return f"Line(n={self.n}, target={self.target:b}, buttons={[f'{b:b}' for b in self.buttons]})"

with open("10.txt", "r") as f:
    lines = [Line(line) for line in f]

ans = 0
ans2 = 0
for line in lines:
    ans += line.solve()
    ans2 += line.solve_lp()
print(ans, ans2)
