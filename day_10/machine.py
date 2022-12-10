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
        """
        each time cycle increases, save what would be current x position, as well as x value
        then loop through saved to print pic
        """

        instructions = input_data.split("\n")

        def _get_pixel(cycle_number, x):
            c = cycle_number
            if 81 > c > 40:
                c = c - 40
            elif 121 > c > 80:
                c = c - 80
            elif 161 > c > 120:
                c = c - 120
            elif 201 > c > 160:
                c = c - 160
            elif 241 > c > 200:
                c = c - 200

            #  have to account for pixel index starting at 0
            # while cycle starts at 1
            if c - 2 == x or c - 1 == x or c == x:
                return "#"

            else:
                return "."

        cycles = 0
        x = 1
        pixels = []
        for instruction in instructions:
            cycles += 1
            pixels.append(_get_pixel(cycles, x))

            if instruction != "noop":
                _, operand = instruction.split(" ")
                cycles += 1
                pixels.append(_get_pixel(cycles, x))
                x += int(operand)

        print("\n")
        for i in range(0, len(pixels), 40):
            print("".join(pixels[i : i + 40]))

        return False
