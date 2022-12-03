import string

from elf_machine import ElfMachine


class Day3(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        rucksacks = input_data.split("\n")
        priority_sum = 0
        for rucksack in rucksacks:
            compartment_size = int(len(rucksack) / 2)
            compartment_one = set(rucksack[:compartment_size])
            compartment_two = set(rucksack[compartment_size:])

            item = compartment_one.intersection(compartment_two).pop()
            priority_sum += string.ascii_letters.index(item) + 1

        return priority_sum

    def solve_second_puzzle(self, input_data: str) -> str:
        groups = input_data.split("\n")
        priority_sum = 0
        for index in range(0, len(groups), 3):
            rucksack_a = set(groups[index])
            rucksack_b = set(groups[index + 1])
            rucksack_c = set(groups[index + 2])

            badge_letter = rucksack_a & rucksack_b & rucksack_c
            priority_sum += string.ascii_letters.index(badge_letter.pop()) + 1

        return priority_sum
