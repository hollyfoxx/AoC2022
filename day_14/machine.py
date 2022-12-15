from elf_machine import ElfMachine


def parse_subpath(sub_path: str):
    x, y = sub_path.split(",")
    return (int(x), int(y))


def print_graph(graph: list):
    print("\n")
    for row in graph[:12]:
        print("".join(row[480:510]))


class Day14(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        row = []
        for _ in range(600):
            row.append(".")

        graph = []
        for _ in range(200):
            graph.append(list(row))

        graph[0][500] = "+"

        paths = input_data.split("\n")
        for path in paths:
            subpaths = path.split(" -> ")
            current = parse_subpath(subpaths[0])
            for subpath in subpaths[1:]:
                next_subpath = parse_subpath(subpath)
                #  same x, different y
                if current[0] == next_subpath[0]:
                    if current[1] < next_subpath[1]:
                        # r
                        for row in range(current[1], next_subpath[1] + 1):
                            graph[row][current[0]] = "#"

                    else:
                        for row in range(next_subpath[1], current[1] + 1):
                            graph[row][current[0]] = "#"

                    for row in range(next_subpath[1], current[1] + 1):
                        graph[row][current[0]] = "#"

                # different x, same y
                elif current[1] == next_subpath[1]:
                    if current[0] < next_subpath[0]:
                        r = range(current[0], next_subpath[0] + 1)
                    else:
                        r = range(next_subpath[0], current[0] + 1)

                    for col in r:
                        graph[current[1]][col] = "#"

                current = next_subpath

        sand_at_rest = 0
        sand = [0, 500]
        try:
            while True:
                while graph[sand[0] + 1][sand[1]] == ".":
                    sand[0] += 1

                if graph[sand[0] + 1][sand[1] - 1] == ".":
                    sand[1] -= 1
                    continue

                if graph[sand[0] + 1][sand[1] + 1] == ".":
                    sand[1] += 1
                    continue

                graph[sand[0]][sand[1]] = "o"
                sand_at_rest += 1
                sand = [0, 500]

                # print_graph(graph)

        except IndexError:
            return sand_at_rest

    def solve_second_puzzle(self, input_data: str) -> int:
        row = []
        for _ in range(800):
            row.append(".")

        graph = []
        for _ in range(200):
            graph.append(list(row))

        graph[0][500] = "+"

        highest_y = 0
        paths = input_data.split("\n")
        for path in paths:
            subpaths = path.split(" -> ")
            current = parse_subpath(subpaths[0])
            for subpath in subpaths[1:]:
                if current[1] > highest_y:
                    highest_y = current[1]

                next_subpath = parse_subpath(subpath)

                #  same x, different y
                if current[0] == next_subpath[0]:
                    if current[1] < next_subpath[1]:
                        # r
                        for row in range(current[1], next_subpath[1] + 1):
                            graph[row][current[0]] = "#"

                    else:
                        for row in range(next_subpath[1], current[1] + 1):
                            graph[row][current[0]] = "#"

                    for row in range(next_subpath[1], current[1] + 1):
                        graph[row][current[0]] = "#"

                # different x, same y
                elif current[1] == next_subpath[1]:
                    if current[0] < next_subpath[0]:
                        r = range(current[0], next_subpath[0] + 1)
                    else:
                        r = range(next_subpath[0], current[0] + 1)

                    for col in r:
                        graph[current[1]][col] = "#"

                current = next_subpath

        floor = highest_y + 2
        for x in range(800):
            graph[floor][x] = "#"

        sand_at_rest = 0
        sand = [0, 500]
        while True:
            while graph[sand[0] + 1][sand[1]] == ".":
                sand[0] += 1

            if graph[sand[0] + 1][sand[1] - 1] == ".":
                sand[1] -= 1
                continue

            if graph[sand[0] + 1][sand[1] + 1] == ".":
                sand[1] += 1
                continue

            graph[sand[0]][sand[1]] = "o"
            # print_graph(graph)
            sand_at_rest += 1

            if sand == [0, 500]:
                break
            sand = [0, 500]

        print_graph(graph)
        return sand_at_rest
