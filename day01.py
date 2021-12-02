from common import *

measurements = pd.DataFrame(
    dict(x=[int(x) for x in get_input(1, 2021).split("\n") if len(x) > 0])
)
print("Day 1, part 1: ", measurements.diff().query("x > 0").size)
print("Day 1, part 2: ", measurements.rolling(3).mean().diff().query("x > 0").size)
