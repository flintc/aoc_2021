from common import *

data_input = get_input(8)


def deduce_output_num(entry):
    df = (pd.Series(
        [set(list(x)) for x in entry.input.split(" ")]).to_frame()
        .assign(length=lambda df: df[0].apply(len))
        .assign(num=lambda df: df.length.replace({7: 8, 3: 7, 4: 4, 2: 1}))
    )
    pos_25 = df.loc[df.num == 1][0].values[0]
    pos_13 = df.loc[df.num == 4][0].values[0].difference(pos_25)
    pos_1235 = df.loc[df.num == 4][0].values[0]

    has_5_segments = df.length == 5
    is_three = df.loc[has_5_segments][0].apply(
        lambda x: pos_25.intersection(x) == pos_25)
    is_five = df.loc[has_5_segments][0].apply(
        lambda x: pos_13.intersection(x) == pos_13)
    is_two = ~(is_three | (is_five))

    has_6_segments = df.length == 6
    is_nine = df.loc[has_6_segments][0].apply(
        lambda x: pos_1235.intersection(x) == pos_1235)
    is_six = df.loc[has_6_segments][0].apply(
        lambda x: pos_13.intersection(x) == pos_13) & ~is_nine
    is_zero = ~(is_nine | (is_six))

    df.loc[is_three.loc[is_three.values].index, "num"] = 3
    df.loc[is_five.loc[is_five.values].index, "num"] = 5
    df.loc[is_two.loc[is_two.values].index, "num"] = 2
    df.loc[is_nine.loc[is_nine.values].index, "num"] = 9
    df.loc[is_six.loc[is_six.values].index, "num"] = 6
    df.loc[is_zero.loc[is_zero.values].index, "num"] = 0

    out = pd.Series([set(list(x)) for x in entry.output.split(" ")]).apply(
        lambda x: list(filter(lambda y: y == x, df[0]))[0]).apply(
        lambda x: df.loc[df[0] == x, "num"].values[0]).values.astype(int).astype(str)
    return int("".join(out))


entries = pd.DataFrame(dict(zip(('input', 'output'), zip(
    *[x.split(" | ") for x in data_input.split("\n") if len(x) > 0]))))
print("Day 8, part 1: ", entries.output.apply(lambda x: x.split(" ")).explode().apply(
    len).to_frame().query("output in [2, 3, 4, 7]").shape[0])

# 1012272
print("Day 8, part 2: ", entries.apply(deduce_output_num, axis=1).sum())
