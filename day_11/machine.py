from math import floor, gcd, lcm
import string

from elf_machine import ElfMachine

class Monkey():
    def __init__(self, id):
        self.items = []
        self._operation = None
        self._operand = None
        self._test_divisor = None
        self.true_monkey = None
        self.false_monkey = None
        self.inspection_count = 0
        self.id = id

    def decrease_worry_level(self, item: int):
        return floor(item / 3)

    def perform_operation(self, item: int):
        if self._operation and self._operand:
            self.inspection_count += 1
            if self._operation == "*":
                if self._operand == "old":
                    return item * item
                else:
                    return item * int(self._operand)

            elif self._operation == "+":
                if self._operand == "old":
                    return item + item
                else:
                    return item + int(self._operand)
    
            return self._operation(item)

        raise NotImplementedError()

    def test_item(self, item: int):
        if self._test_divisor:
            if item % self._test_divisor == 0:
                return self.true_monkey
            
            return self.false_monkey

        raise NotImplementedError()

class Day11(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        monkeys = input_data.split('\n\n')

        parsed_monkeys = []
        for index, m in enumerate(monkeys):
            metadata = m.split('\n')
            monkey = Monkey(index)
            starting_items = metadata[1].split(": ")[1].split(", ")
            monkey.items = [int(i) for i in starting_items]

            operation, operand = metadata[2].split("old ")[1].split(" ")
            monkey._operation = operation
            monkey._operand = operand 
        
            monkey._test_divisor = int(metadata[3].split("divisible by")[1])
            monkey.true_monkey = int(metadata[4].split("monkey ")[1])
            monkey.false_monkey = int(metadata[5].split("monkey ")[1])

            parsed_monkeys.append(monkey)

        index = 0
        for round in range(0, 20):
            for monkey in parsed_monkeys:
                for item in monkey.items:
                    worry_level = monkey.perform_operation(item)
                    worry_level = monkey.decrease_worry_level(worry_level)
                    dest_monkey_index = monkey.test_item(worry_level)
                    parsed_monkeys[dest_monkey_index].items.append(worry_level)
                
                monkey.items = []

        inspection_count = sorted([monkey.inspection_count for monkey in parsed_monkeys])
        monkey_business = inspection_count.pop() * inspection_count.pop()
        return monkey_business

    def solve_second_puzzle(self, input_data: str) -> str:
        monkeys = input_data.split('\n\n')

        parsed_monkeys = []
        for index, m in enumerate(monkeys):
            metadata = m.split('\n')
            monkey = Monkey(index)
            starting_items = metadata[1].split(": ")[1].split(", ")
            monkey.items = [int(i) for i in starting_items]

            operation, operand = metadata[2].split("old ")[1].split(" ")
            monkey._operation = operation
            monkey._operand = operand 
        
            monkey._test_divisor = int(metadata[3].split("divisible by")[1])
            monkey.true_monkey = int(metadata[4].split("monkey ")[1])
            monkey.false_monkey = int(metadata[5].split("monkey ")[1])

            parsed_monkeys.append(monkey)

        mod = lcm(*[monkey._test_divisor for monkey in parsed_monkeys])

        index = 0
        for round in range(0, 10000):
            for monkey in parsed_monkeys:
                for item in monkey.items:
                    worry_level = monkey.perform_operation(item)
                    dest_monkey_index = monkey.test_item(worry_level)
                    parsed_monkeys[dest_monkey_index].items.append(worry_level % mod)
                
                monkey.items = []


        inspection_count = sorted([monkey.inspection_count for monkey in parsed_monkeys])
        monkey_business = inspection_count.pop() * inspection_count.pop()
        return monkey_business