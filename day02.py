from common import *

parsed = [x.split(" ") for x in get_input(2, 2021).split("\n") if len(x) > 0]
df = pd.DataFrame(dict(zip(["dir", "amount"], zip(*parsed)))).astype({"amount": int})
df = df.assign(
    y=df.dir.apply(lambda d: 1 if d == "down" else -1 if d == "up" else 0),
    x=df.dir.apply(lambda d: 1 if d == "forward" else 0),
)
df = df.assign(pos=df.x * df.amount, depth=df.y * df.amount)
part1 = df.sum()
part2 = df.assign(depth=df.depth.cumsum() * df.pos).sum()

print("Day 2, part 1: ", part1.depth * part1.pos)
print("Day 2, part 2: ", part2.depth * part2.pos)
