from common import *

data = np.array(get_input(6).replace("\n", "").split(",")).astype(np.int8)


def simulate_lanternfish(initial_state, num_days):
    prev_state = initial_state.copy()
    for _ in range(num_days):
        state = Counter()
        for ix in range(9):
            state[ix % 9] = prev_state[(ix + 1) % 9]
        state[6] += prev_state[0]
        prev_state = state
    return state


print("Day 6, part 1:", sum(simulate_lanternfish(Counter(data), 80).values()))
print("Day 6, part 2:", sum(simulate_lanternfish(Counter(data), 256).values()))
