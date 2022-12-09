import string

from elf_machine import ElfMachine


def is_visible(rows: list[str], row_index: int, col_index: int):
    tree_height = int(rows[row_index][col_index])

    #  check left
    left_visible = True
    c = col_index
    while c > 0:
        c -= 1
        if int(rows[row_index][c]) >= tree_height:
            left_visible = False

    #  check down
    down_visible = True
    r = row_index
    while r < len(rows[0]) - 1:
        r += 1
        if int(rows[r][col_index]) >= tree_height:
            down_visible = False

    #  check right
    right_visible = True
    c = col_index
    while c < len(rows[0]) - 1:
        c += 1
        if int(rows[row_index][c]) >= tree_height:
            right_visible = False

    #  check up
    up_visible = True
    r = row_index
    while r > 0:
        r -= 1
        if int(rows[r][col_index]) >= tree_height:
            up_visible = False

    return left_visible or down_visible or right_visible or up_visible


def calculate_scenic_score(rows: list[str], row_index: int, col_index: int):
    tree_height = int(rows[row_index][col_index])

    #  check up
    up_score = 0
    r = row_index
    while r > 0:
        r -= 1
        up_score += 1
        if int(rows[r][col_index]) >= tree_height:
            break

    #  check left
    left_score = 0
    c = col_index
    while c > 0:
        c -= 1
        left_score += 1
        if int(rows[row_index][c]) >= tree_height:
            break

    #  check down
    down_score = 0
    r = row_index
    while r < len(rows[0]) - 1:
        r += 1
        down_score += 1
        if int(rows[r][col_index]) >= tree_height:
            break

    #  check right
    right_score = 0
    c = col_index
    while c < len(rows[0]) - 1:
        c += 1
        right_score += 1
        if int(rows[row_index][c]) >= tree_height:
            break

    return up_score * left_score * down_score * right_score


class Day8(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        rows = input_data.split("\n")
        visible = (2 * len(rows)) + (2 * len(rows[0])) - 4

        for row_index, row in enumerate(rows):
            if row_index == 0 or row_index == len(rows) - 1:
                continue

            for col_index, _ in enumerate(row):
                if col_index == 0 or col_index == len(row) - 1:
                    continue

                if is_visible(rows, row_index, col_index):
                    visible += 1

        return visible

    def solve_second_puzzle(self, input_data: str) -> str:
        rows = input_data.split("\n")
        scenic_scores = []

        for row_index, row in enumerate(rows):
            if row_index == 0 or row_index == len(rows) - 1:
                continue

            for col_index, _ in enumerate(row):
                if col_index == 0 or col_index == len(row) - 1:
                    continue

                scenic_scores.append(calculate_scenic_score(rows, row_index, col_index))

        return max(scenic_scores)
