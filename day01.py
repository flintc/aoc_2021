from common import *

raw_data = get_input(1, 2021)

measurements = [int(x) for x in raw_data.split("\n") if len(x) > 0]
increased, = np.where(np.diff(measurements)>0)
print("Day 1, part 1: ", len(increased))

measurements = [int(x.split(" ")[0]) for x in raw_data.split("\n") if len(x) > 0]
measurements_rolling_avg = np.convolve(measurements, np.ones(3), 'valid')
increased, = np.where(np.diff(measurements_rolling_avg)>0)
print("Day 1, part 2: ", len(increased))
