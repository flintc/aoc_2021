from common import *

raw_data = get_input(2, 2021)
df = pd.DataFrame([dict(
    direction=x.split(" ")[0], amount=float(x.split(" ")[1]))
    for x in raw_data.split("\n") if len(x) > 0])

df = df.assign(
    y=df.direction
    .mask(df.direction == "forward", 0)
    .mask(df.direction == "down", 1)
    .mask(df.direction == "up", -1),
    x=df.direction
    .mask(df.direction != "forward", 0)
    .mask(df.direction == "forward", 1),
)
df = df.assign(pos=df.x * df.amount)

df_part1 = df.assign(depth=df.y * df.amount).sum(axis=0)
print("Day 2, part 1: ", df_part1.depth * df_part1.pos)

df_part2 = df.assign(depth=(df.y * df.amount).cumsum()*df.pos).sum(axis=0)
print("Day 2, part 2: ", df_part2.depth * df_part2.pos)
