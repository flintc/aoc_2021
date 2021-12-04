from common import *

data_input = get_input(4)
numbers = data_input.split("\n\n")[0]
boards = [[list(filter(lambda z: len(z) > 0, y.split(" ")))
          for y in x.split("\n") if len(y) > 0] for x in data_input.split("\n\n")[1::]]
dfs = []
num = 0
for b in boards:
    board = np.array(b).astype(int)
    options = dict(enumerate(np.vstack([board, board.T])))
    dfs.append(pd.DataFrame(options).T.assign(board=num).reset_index())
    num += 1
boards_df = pd.concat(dfs).reset_index(drop=True).set_index(["board", "index"])


def main():
    # Part 1
    game_df = boards_df.copy()
    for num in numbers.split(","):
        game_df = game_df.mask(game_df == int(num), -1)
        check = game_df.mask(game_df == 1, -1).sum(axis=1) == -5
        if check.sum() > 0:
            break
    winner = check.loc[check == True].index[0][0]
    winner_board = game_df.loc[winner].head(int(game_df.loc[winner].shape[0]/2))
    print("Day 4, part 1", winner_board.mask(
        winner_board == -1, 0).sum().sum() * int(num))

    game_df = boards_df.copy()

    # Part 2
    num_boards = len(boards_df.groupby(["board"]).groups.keys())
    for num in numbers.split(","):
        game_df = game_df.mask(game_df == int(num), -1)
        check = game_df.mask(game_df == 1, -1).sum(axis=1) == -5
        if (check.groupby(["board"]).describe().unique == 2).sum() == num_boards-1:
            is_loser = (check.groupby(["board"]).describe().unique == 1)
            loser = is_loser.loc[is_loser == True].index[0]
        if (check.groupby(["board"]).describe().unique == 2).sum() == num_boards:
            break

    loser_board = game_df.loc[loser].head(int(game_df.loc[loser].shape[0]/2))
    print("Day 4, part 2", loser_board.mask(loser_board == -1, 0).sum().sum() * int(num))


if __name__ == "__main__":
    main()
