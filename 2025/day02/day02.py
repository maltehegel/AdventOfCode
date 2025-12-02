import time


def read_puzzle() -> list[list[int]]:
    line = ""
    with open("input.txt", "r") as f:
        line = f.read()
        f.close()

    input = line.split(",")
    ranges = [[]]
    for i in input:
        _ = i.split("-")
        start = _[0]
        end = _[1]
        ranges.append([int(start), int(end.strip("\n"))])
    ranges.remove([])
    return ranges


def solve_pt1(puzzle: list[list[int]]) -> int:
    solution = 0
    for i in puzzle:
        start = i[0]
        end = i[1]

        for num in range(start, end + 1):
            num_to_string = str(num)
            len_num = len(num_to_string)
            half_len = int(len_num / 2)
            if num_to_string[:half_len] == num_to_string[half_len:]:
                solution += num

    return solution


def solve_pt2(puzzle: list[list[int]]) -> int:
    solution = 0
    for p in puzzle:
        start = p[0]
        end = p[1]
        prev = -1
        for current_num in range(start, end + 1):
            num_to_string = str(current_num)
            len_num = len(num_to_string)

            for slice in range(1, len_num):
                if len_num % slice == 0:
                    multiples = int(len_num / slice)

                    for m in range(2, multiples + 1):
                        if (
                            num_to_string[:slice]
                            == num_to_string[(m - 1) * slice : (m) * slice]
                        ):
                            if m == multiples and prev != current_num:
                                solution += current_num
                                prev = current_num
                        else:
                            break
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
