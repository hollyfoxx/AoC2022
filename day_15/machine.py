from elf_machine import ElfMachine
import re


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
        only_possible_beacon = []
        line_of_interest = set(range(0, 20))

        parsed = []
        for line in input_data.split("\n"):
            sensor_x, beacon_x = [int(x) for x in re.findall(r"[x]=(-?\d+)", line)]
            sensor_y, beacon_y = [int(x) for x in re.findall(r"[y]=(-?\d+)", line)]

            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            parsed.append((sensor_x, beacon_x, sensor_y, beacon_y, distance))

        for y in range(0, 20):
            not_beacons = set()
            for data_points in parsed:
                sensor_x, beacon_x, sensor_y, beacon_y, distance = data_points
                difference = abs(y - sensor_y)  # example input
                r = set(
                    range(
                        sensor_x - (distance - difference),
                        sensor_x + (distance - difference) + 1,
                    )
                )

                not_beacons = not_beacons | r
            could_be_beacons = line_of_interest - not_beacons
            for b in could_be_beacons:
                only_possible_beacon.append((b, y))
                break
        return (only_possible_beacon[0][0] * 4000000) + only_possible_beacon[0][1]
