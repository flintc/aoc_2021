from common import *


def to_dec(df):
    return int("".join(df.values.flatten()), base=2)


def get_rating(df, least_common=False, tie_breaker='1'):
    new_df = df.copy()
    inc = 0
    max_pos = len(df.columns)
    while True:
        pos = inc % max_pos
        value_counts = new_df[pos].value_counts(ascending=least_common)
        if value_counts.unique().size == 1:
            new_df = new_df.loc[new_df[pos] == tie_breaker]
        else:
            new_df = new_df.loc[new_df[pos] == value_counts.index[0]]
        if new_df.shape[0] == 1:
            break
        inc += 1
    return new_df.pipe(to_dec)


def main():
    raw_data = get_input(3)
    df = pd.DataFrame([list(x) for x in raw_data.split("\n") if len(x) > 0])
    value_counts = df.apply(pd.Series.value_counts)
    gamma = value_counts.apply(lambda col: col.sort_values().index[-1]).pipe(to_dec)
    epsilon = value_counts.apply(lambda col: col.sort_values().index[0]).pipe(to_dec)

    print("Day 3, part 1: ", gamma * epsilon)
    print("Day 3, part 2: ", get_rating(df, False, '1')*get_rating(df, True, '0'))


if __name__ == "__main__":
    main()
