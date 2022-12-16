from elf_machine import ElfMachine
import re
from tqdm import tqdm


class Day15(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        not_beacons = set()
        for line in input_data.split("\n"):
            sensor_x, beacon_x = [int(x) for x in re.findall(r"[x]=(-?\d+)", line)]
            sensor_y, beacon_y = [int(x) for x in re.findall(r"[y]=(-?\d+)", line)]

            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            # difference = abs(10 - sensor_y) // example input
            difference = abs(2000000 - sensor_y)  # puzzle input
            r = set(
                range(
                    sensor_x - (distance - difference),
                    sensor_x + (distance - difference),
                )
            )
            not_beacons = not_beacons | r

        return len(not_beacons)

    def solve_second_puzzle(self, input_data: str) -> int:
        parsed = []
        for line in input_data.split("\n"):
            sensor_x, beacon_x = [int(x) for x in re.findall(r"[x]=(-?\d+)", line)]
            sensor_y, beacon_y = [int(x) for x in re.findall(r"[y]=(-?\d+)", line)]

            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            parsed.append((sensor_x, sensor_y, distance))

        for upper in tqdm(range(5_000, 4_000_001, 5_000)):
            lower = upper - 5_000
            for i_upper in tqdm(range(5_000, 4_000_001, 5_000)):
                i_lower = i_upper - 5_000
                # for upper in tqdm(range(500, 4_000_001, 500)):
                #     lower = upper - 500

                # print(i_lower, i_upper)
                # print(lower, upper)

                line_of_interest = set(range(lower, upper))
                for y in range(i_lower, i_upper):
                    # print(y)
                    not_beacons = set()
                    for data_points in parsed:
                        sensor_x, sensor_y, distance = data_points
                        difference = abs(y - sensor_y)

                        start = max(lower, sensor_x - (distance - difference))
                        end = min(sensor_x + (distance - difference) + 1, upper)
                        if (start < lower and end < lower) or (
                            start > upper and end > upper
                        ):
                            continue

                        r = set(
                            range(
                                start,
                                end,
                            )
                        )

                        not_beacons = not_beacons | r

                    could_be_beacons = line_of_interest - not_beacons
                    if could_be_beacons:
                        # print(could_be_beacons)
                        return (list(could_be_beacons)[0] * 4000000) + y
