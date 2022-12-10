from elf_machine import ElfMachine


class Day10(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        instructions = input_data.split("\n")

        interesting_cycles = [20, 60, 100, 140, 180, 220]
        signal_strength_sums = 0

        cycles = 0
        x = 1
        print("\n")
        for instruction in instructions:
            cycles += 1
            if cycles in interesting_cycles:
                signal_strength_sums += cycles * x

            if instruction != "noop":
                _, operand = instruction.split(" ")
                cycles += 1
                if cycles in interesting_cycles:
                    signal_strength_sums += cycles * x
                x += int(operand)

        return signal_strength_sums

    def solve_second_puzzle(self, input_data: str) -> str:
        return False
