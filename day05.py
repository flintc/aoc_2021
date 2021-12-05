from common import *


def to_points_vh(line_segment, orientation):
    const = "x" if orientation == "v" else "y"
    var = "y" if const == "x" else "x"
    rng = line_segment[var+"2"] - line_segment[var+"1"]
    return pd.DataFrame({
        const: [line_segment[const+"1"]] * (abs(rng) + 1),
        var: list(
            range(
                min(line_segment[var+"1"], line_segment[var+"2"]),
                max(line_segment[var+"1"], line_segment[var+"2"]) + 1))
    })


def to_points(x):
    if (x.x1 == x.x2):
        return to_points_vh(x, "v")
    elif (x.y1 == x.y2):
        return to_points_vh(x, "h")
    else:
        def maybe_reversed(x): return x
        if (x.x1 > x.x2 and x.y1 < x.y2) or (x.x1 < x.x2 and x.y1 > x.y2):
            maybe_reversed = reversed
        return pd.DataFrame(
            dict(
                x=list((range(min(x.x1, x.x2), max(x.x1, x.x2)+1))),
                y=list(maybe_reversed(range(min(x.y1, x.y2), max(x.y1, x.y2)+1)))
            ),

        )


def get_num_overlaps(df, exclude_diagonal=False):
    return (
        df
        .query("x1 == x2 or y1 == y2" if exclude_diagonal else "x1 == x1")
        .apply(to_points, axis=1)
        .pipe(lambda s: pd.concat(s.values))
        .groupby(["x", "y"]).x.count())


def main():
    df = pd.DataFrame(dict(zip(("x1", "y1", "x2", "y2"), zip(
        *re.findall("([0-9]+),([0-9]+)(?:\s->\s)([0-9]+),([0-9]+)", get_input(5)))))).astype(int)
    num_overlaps = get_num_overlaps(df, True)
    print("Day 5, part 1:", num_overlaps.loc[num_overlaps >= 2].shape[0])
    num_overlaps = get_num_overlaps(df, False)
    print("Day 5, part 2:", num_overlaps.loc[num_overlaps >= 2].shape[0])


if __name__ == "__main__":
    main()
