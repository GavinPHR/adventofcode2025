class Shape:
    def __init__(self, lines):
        self.lines = [line.strip() for line in lines[1:]]
        self.solid = 0
        for line in lines:
            for c in line:
                if c == "#":
                    self.solid += 1

    def __repr__(self):
        return f"Shape(solid={self.solid}, lines={self.lines})"

class Region:
    def __init__(self, line):
        parts = line.strip().split()
        self.b, self.h = map(int, parts[0][:-1].split("x"))
        self.nums = list(map(int, parts[1:]))

    def __repr__(self):
        return f"Region(b={self.b}, h={self.h}, nums={self.nums})"

shapes = []
regions = []
lines = []
with open("12.txt", "r") as f:
    for line in f:
        if line == "\n":
            shapes.append(Shape(lines))
            lines = []
        elif "x" in line:
            regions.append(Region(line))
        else:
            lines.append(line)

ans = 0
for region in regions:
    required = 0
    for i, num in enumerate(region.nums):
        required += num * shapes[i].solid
    if required <= region.b * region.h:
        ans += 1
print(ans)
