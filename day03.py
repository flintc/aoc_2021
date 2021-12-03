from common import *


def binary_df_to_decimal(df):
    return int("".join(df.values.flatten()), base=2)


def get_rate(df, least_common=False):
    return (df.apply(pd.Series.value_counts)
              .apply(lambda col: col.sort_values(ascending=least_common).index[0])
              .pipe(binary_df_to_decimal))


def get_rating(df, least_common=False, tie_breaker='1'):
    new_df = df.copy()
    inc = 0
    while True:
        pos = inc % len(df.columns)
        value_counts = new_df[pos].value_counts(ascending=least_common)
        keep = tie_breaker if value_counts.unique().size == 1 else value_counts.index[0]
        new_df = new_df.loc[new_df[pos] == keep]
        if new_df.shape[0] == 1:
            break
        inc += 1
    return new_df.pipe(binary_df_to_decimal)


def main():
    df = pd.DataFrame([list(x) for x in get_input(3).split("\n") if len(x) > 0])
    print("Day 3, part 1: ", get_rate(df, False) * get_rate(df, True))
    print("Day 3, part 2: ", get_rating(df, False, '1') * get_rating(df, True, '0'))


if __name__ == "__main__":
    main()
