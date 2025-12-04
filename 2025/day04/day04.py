import time

roll = "@"
accessable_roll = "x"
removed_roll = "-"
max_adjacent_rolls = 4


def read_puzzle():
    puzzle = []
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()
    return puzzle


def solve_pt1(grid):
    solution = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            slot = grid[row][column]

            if slot == roll:
                adjacent_rolls = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if row + i < 0 or column + j < 0:
                            continue
                        elif i == 0 and j == 0:
                            continue
                        try:
                            cell_to_check = grid[row + i][column + j]
                        except IndexError:
                            continue
                        if cell_to_check == roll or cell_to_check == accessable_roll:
                            adjacent_rolls += 1
                if adjacent_rolls < max_adjacent_rolls:
                    solution += 1

    return solution


def check_neighbors_and_remove(row, column, grid) -> int:
    if grid[row][column] == removed_roll:
        return 0
    solution = 0
    adjacent_rolls = 0
    nearby_rolls = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i < 0 or column + j < 0:
                continue
            elif i == 0 and j == 0:
                continue
            try:
                cell_to_check = grid[row + i][column + j]
            except IndexError:
                continue
            if cell_to_check == roll or cell_to_check == accessable_roll:
                adjacent_rolls += 1
                nearby_rolls.append([row + i, column + j])

    if adjacent_rolls < max_adjacent_rolls:
        solution += 1
        row_string = grid[row]
        grid[row] = row_string[:column] + removed_roll + row_string[column + 1 :]
        for rolls in nearby_rolls:
            solution += check_neighbors_and_remove(rolls[0], rolls[1], grid)
        return solution
    return 0


def solve_pt2(grid):
    solution = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            slot = grid[row][column]

            if slot == roll:
                solution += check_neighbors_and_remove(row, column, grid)

    return solution


if __name__ == "__main__":
    puzzle = read_puzzle()

    t_pt1_start = time.time()
    solution_pt1 = solve_pt1(puzzle)
    t_pt1_end = time.time()
    pt1_total = t_pt1_end - t_pt1_start

    t_pt2_start = time.time()
    solution_pt2 = solve_pt2(puzzle)
    t_pt2_end = time.time()
    pt2_total = t_pt2_end - t_pt2_start

    print(f"solution to pt1 is {solution_pt1}, took: {pt1_total:.3f} seconds")
    print(f"solution to pt2 is {solution_pt2}, took: {pt2_total:.3f} seconds")
