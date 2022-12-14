import string

from elf_machine import ElfMachine


class Day6(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        potential_marker = list(input_data[:4])
        if len(set(potential_marker)) == 4:
            return 4
        
        else:
            count = 5
            for letter in input_data[4:]:
                potential_marker.pop(0)
                potential_marker.append(letter)
                if len(set(potential_marker)) == 4:
                    return count

                count +=1
                
    def solve_second_puzzle(self, input_data: str) -> str:
        potential_marker = list(input_data[:14])
        if len(set(potential_marker)) == 14:
            return 14
        
        else:
            count = 15
            for letter in input_data[14:]:
                potential_marker.pop(0)
                potential_marker.append(letter)
                if len(set(potential_marker)) == 14:
                    return count

                count +=1