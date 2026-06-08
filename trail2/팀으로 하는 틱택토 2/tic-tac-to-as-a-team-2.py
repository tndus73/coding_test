board = [input() for _ in range(3)]

lines = []

for i in range(3):
    lines.append(board[i])
    lines.append(board[0][i] + board[1][i] + board[2][i])

lines.append(board[0][0] + board[1][1] + board[2][2])
lines.append(board[0][2] + board[1][1] + board[2][0])

teams = set()

for line in lines:
    s = set(line)

    if len(s) == 2:
        teams.add(tuple(sorted(s)))
print(len(teams))

